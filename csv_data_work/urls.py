from django.urls import path

from csv_data_work.views import index, SchemaListView, SchemaCreateView, \
    SchemaUpdateView, SchemaDeleteView, SchemaDetailView

urlpatterns = [
    path("", index, name="index"),
    path("schemas/", SchemaListView.as_view(), name="schema-list"),
    path("schemas/<int:pk>/", SchemaDetailView.as_view(), name="schema-detail"),
    path("schemas/create/", SchemaCreateView.as_view(), name="schema-create"),
    path(
        "schemas/<int:pk>/update",
        SchemaUpdateView.as_view(),
        name="schema-update"
    ),
    path(
        "schemas/<int:pk>/delete",
        SchemaDeleteView.as_view(),
        name="schema-delete"
    )
]

app_name = "csv_data_work"
