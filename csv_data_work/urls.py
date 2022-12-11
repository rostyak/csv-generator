from django.urls import path

from csv_data_work.views import index, SchemaListView, SchemaCreateView

urlpatterns = [
    path("", index, name="index"),
    path("schemas/", SchemaListView.as_view(), name="schema-list"),
    path("schemas/create/", SchemaCreateView.as_view(), name="schema-create")
]

app_name = "csv_data_work"
