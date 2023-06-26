from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse
from django.apps import apps
from django.contrib import messages
from django.db import models
from django.db.models import ObjectDoesNotExist
from django.utils.dateparse import parse_datetime


def load_default(request):
    return render(request, "base.html")


def load_table_names_selected():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
        )
        tables = [row[0] for row in cursor.fetchall()]

    tables = [name for name in tables if not name.startswith(("django", "auth", "sys"))]
    return tables


def table_list_view(request):
    filtered_table_names = load_table_names_selected()
    return render(request, "table_list.html", {"table_names": filtered_table_names})


def load_from_table(table_name):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}';"
        )
        columns = [row[0] for row in cursor.fetchall()]

        cursor.execute(f"SELECT * FROM {table_name};")
        data = cursor.fetchall()
        return data, columns


def table_detail_view(request, table_name):
    data, columns = load_from_table(table_name)
    return render(
        request,
        "table_detail.html",
        {"table_name": table_name, "columns": columns, "data": data},
    )


def print_all_models(app_label):
    app_config = apps.get_app_config(app_label)
    for model in app_config.models.values():
        print(model.__name__)


def update_table(request):
    if request.method == "POST" and request.is_ajax():
        table_name = request.POST.get("table_name")
        row_data = request.POST.getlist("row_data[]")
        row_id = row_data[0]

        # Retrieve the table model based on the table name
        table_model = apps.get_model(app_label="dbms", model_name=table_name)
        identifier_field = table_model._meta.pk

        try:
            table_instance = get_object_or_404(
                table_model, **{identifier_field.name: row_id}
            )

            # Update the model instance with the new data
            for i, column in enumerate(table_model._meta.fields):
                if column != identifier_field:
                    new_value = row_data[i]
                    if column.is_relation:
                        # Handle foreign key fields
                        related_model = column.related_model
                        try:
                            related_object = related_model.objects.get(pk=new_value)
                            setattr(table_instance, column.name, related_object)
                        except ObjectDoesNotExist:
                            return JsonResponse(
                                {
                                    "error": f"Related object not found for {column.name}"
                                },
                                status=400,
                            )
                    elif column.get_internal_type() == "DateTimeField":
                        # Handle DateTimeField
                        try:
                            datetime_value = parse_datetime(new_value)
                            if datetime_value is not None:
                                # If a valid datetime value is parsed, assign it to the field
                                setattr(table_instance, column.name, datetime_value)
                            else:
                                # If the parsing fails, try parsing as date only
                                date_value = parse_datetime(new_value)
                                if date_value is not None:
                                    # If a valid date value is parsed, assign it to the field
                                    setattr(table_instance, column.name, date_value)
                        except ValidationError:
                            return JsonResponse(
                                {"error": f"Invalid datetime format for {column.name}"},
                                status=400,
                            )
                    else:
                        setattr(table_instance, column.name, new_value)

            # Save the updated model instance to the database
            table_instance.save()

            return JsonResponse({"success": "Table updated successfully"})
        except table_model.DoesNotExist:
            return JsonResponse({"error": "Table not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)


def delete_row(request):
    if request.method == "POST":
        table_name = request.POST.get("table_name")
        row_data = request.POST.getlist("row_data[]")

        # Perform the cascade effect check if the row contains foreign keys
        try:
            table_model = apps.get_model(app_label="dbms", model_name=table_name)
            related_fields = [
                field
                for field in table_model._meta.get_fields()
                if isinstance(field, models.ForeignKey)
            ]
            related_models = [field.related_model for field in related_fields]
            related_field_names = [field.name for field in related_fields]

            # Check if the row's foreign key fields are non-null and have related objects
            cascade_effect = False
            cascade_models = []
            for model, field_name in zip(related_models, related_field_names):
                field_value = row_data[table_model._meta.get_field(field_name).column]

                # Check if the field is a string-based primary key
                field = table_model._meta.get_field(field_name)
                if field.primary_key and isinstance(field_value, str):
                    field_value = field.to_python(field_value)

                if field_value and model.objects.filter(pk=field_value).exists():
                    cascade_effect = True  # Assign the value here
                    cascade_models.append(model)

            if cascade_effect:
                # Prepare the confirmation message
                message = "Deleting this row will have a cascade effect on the following models:\n"
                for model in cascade_models:
                    message += f"- {model._meta.verbose_name_plural}\n"
                message += "Are you sure you want to proceed?"

                return JsonResponse({"cascade": True, "message": message})

            primary_key_field_name = table_model._meta.pk.name

            try:
                # Extract the primary key value from row_data
                primary_key_value = row_data[
                    0
                ]  # Assuming the primary key value is in the first position

                # Check if the primary key is a string-based field
                primary_key_field = table_model._meta.get_field(primary_key_field_name)
                if isinstance(primary_key_field, models.CharField):
                    primary_key_value = primary_key_field.to_python(primary_key_value)

                # Fetch the specific row from the table using the primary key value
                row = table_model.objects.get(
                    **{primary_key_field_name: primary_key_value}
                )

                # Delete the row
                row.delete()

                # Reload the table
                return render(request, "table_detail.html")

            except table_model.DoesNotExist:
                return HttpResponse("Row does not exist.")
            except Exception as e:
                return HttpResponse(f"Error deleting row: {str(e)}")

        except LookupError:
            return JsonResponse({"error": "Invalid table name"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)


def order_table(request, table_name, column_name):
    # Retrieve the table model based on the table name
    table_model = apps.get_model(app_label="dbms", model_name=table_name)

    # Convert the column name to lowercase for comparison
    column_name_lower = column_name.lower()

    # Check if the specified column exists in the table
    column_names = [field.name for field in table_model._meta.fields if field.db_column]
    if column_name_lower not in [name.lower() for name in column_names]:
        return JsonResponse({"error": "Invalid column name"}, status=400)

    # Get the primary key field name
    primary_key_field_name = table_model._meta.pk.name

    # Retrieve the current order from the session
    order = request.session.get("order", {})
    current_order_column = order.get("column")
    current_order_direction = order.get("direction")

    # Determine the new order column and direction
    if current_order_column == column_name_lower:
        # If the same column is clicked again, toggle the order direction
        if current_order_direction == "asc":
            new_order_direction = "desc"
        else:
            new_order_direction = "asc"
    else:
        # If a new column is clicked, set the order direction to ascending
        new_order_direction = "asc"

    # Update the session with the new order
    request.session["order"] = {
        "column": column_name_lower,
        "direction": new_order_direction,
    }

    # Check if the column is a BinaryField
    field_type = table_model._meta.get_field(column_name_lower).get_internal_type()
    if field_type == "BinaryField":
        # Display an error message on the table_detail page
        messages.error(request, "Table cannot be ordered by BinaryField data type!")

        # Fetch the column names from the database using raw SQL query
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}';"
            )
            columns = [row[0] for row in cursor.fetchall()]

        # Prepare the data to be passed to the template
        table_data = []

        context = {
            "table_name": table_name,
            "columns": columns,
            "data": table_data,
        }

        return render(request, "table_detail.html", context)

    # Determine the ordering string based on the new order
    ordering = (
        f"{column_name_lower}"
        if new_order_direction == "asc"
        else f"-{column_name_lower}"
    )

    # Retrieve all rows from the table and order them by the specified column
    rows = table_model.objects.all().order_by(ordering)

    # Fetch the column names from the database using raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}';"
        )
        columns = [row[0] for row in cursor.fetchall()]

    # Prepare the data to be passed to the template
    table_data = []
    for row in rows:
        row_data = [getattr(row, primary_key_field_name)]
        for name in columns:
            if name.lower() != primary_key_field_name:
                # Check if the field is a foreign key
                field = table_model._meta.get_field(name.lower())
                if field.is_relation:
                    # Retrieve the related object
                    related_object = getattr(row, name.lower())
                    if related_object is not None:
                        # Get the related field's value
                        related_value = getattr(related_object, field.target_field.name)
                        row_data.append(related_value)
                    else:
                        row_data.append(None)
                else:
                    row_data.append(getattr(row, name.lower()))
        table_data.append(row_data)

    context = {
        "table_name": table_name,
        "columns": columns,
        "data": table_data,
    }

    return render(request, "table_detail.html", context)


def get_columns(request, table_name):
    if not table_name:
        return JsonResponse({"error": "Table name is required"}, status=400)

    table_model = apps.get_model(app_label="dbms", model_name=table_name.lower())
    column_names = [field.name for field in table_model._meta.fields if field.db_column]

    return JsonResponse(column_names, safe=False)


def load_data_ordered(table_name, order, dir):
    table_model = apps.get_model(app_label="dbms", model_name=table_name)
    field_type = table_model._meta.get_field(order.lower()).get_internal_type()
    if field_type != "BinaryField":
        with connection.cursor() as cursor:
            if dir == "DESC":
                cursor.execute(f"SELECT * FROM {table_name} ORDER BY {order} DESC;")
                data = cursor.fetchall()
            else:
                cursor.execute(f"SELECT * FROM {table_name} ORDER BY {order} ASC;")
                data = cursor.fetchall()
            return data
    elif field_type == "BinaryField":
        return None


def load_tables(request):
    tables = load_table_names_selected()
    table_name = request.POST.get("table")
    column_name = request.POST.get("column")
    column_order = request.POST.get("column-order")
    context = {"tables": tables}
    if table_name is not None:
        if column_name is not None:
            data, columns = load_from_table(table_name)
            data = load_data_ordered(table_name, column_name, column_order)
            if data is None:
                messages.error(request, "Cannot order by BinaryField!")
            else:
                context = {
                    "tables": tables,
                    "table_name": table_name,
                    "table_data": data,
                    "table_columns": columns,
                }
        else:
            data, columns = load_from_table(table_name)
            context = {
                "tables": tables,
                "table_name": table_name,
                "table_data": data,
                "table_columns": columns,
            }
    return render(request, "analytics.html", context)
