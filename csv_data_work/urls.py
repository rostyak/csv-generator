from django.urls import path, include

from csv_data_work.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "csv_data_work"
