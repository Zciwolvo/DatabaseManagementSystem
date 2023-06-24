from django.test import TestCase
from django.urls import reverse
from django.apps import apps


class OrderTableTest(TestCase):
    def test_table_loading(self):
        # Get all the table names in the database
        table_names = apps.all_models.keys()
        table_names = [
            name
            for name in table_names
            if not name.startswith(("django", "auth", "sys"))
        ]

        # Iterate through each table
        for table_name in table_names:
            # Get the table model
            table_model = apps.get_model(app_label="dbms", model_name=table_name)

            # Iterate through each column in the table
            for column in table_model._meta.fields:
                # Construct the URL to the order_table view for the current table and column
                url = reverse("order_table", args=[table_name, column.name])

                # Send a GET request to the URL and check if the response is successful
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

                # You can add additional assertions to check if the response content is correct
                # For example, you can check if the column name is displayed correctly in the response
                self.assertContains(response, column.name)
