from django.urls import path, include

from csv_data_work.views import index, SchemaListView

urlpatterns = [
    path("", index, name="index"),
    path("schemas/", SchemaListView.as_view(), name="schema-list")
]

app_name = "csv_data_work"
