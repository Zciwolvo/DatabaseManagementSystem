from django.contrib import admin
from django.urls import path
from dbms.views import (
    table_list_view,
    table_detail_view,
    update_table,
    order_table,
    load_tables,
    get_columns,
    delete_row,
    load_default,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", load_default, name="load_default"),
    path("tables/", table_list_view, name="table_list"),
    path("tables/<str:table_name>/", table_detail_view, name="table_detail"),
    path("update_table/", update_table, name="update_table"),
    path("<str:table_name>/order/<str:column_name>/", order_table, name="order_table"),
    path("analytics/", load_tables, name="load_tables"),
    path("get_columns/<str:table_name>/", get_columns, name="get_columns"),
    path("delete_row/", delete_row, name="delete_row"),
]
