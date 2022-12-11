from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from csv_data_work.models import Schema


def index(request):
    return render(request, "csv_data_work/index.html")


class SchemaListView(LoginRequiredMixin, generic.ListView):
    model = Schema
    queryset = Schema.objects.all()
    template_name = "csv_data_work/schema_list.html"
    context_object_name = "schema_list"

    def get_queryset(self):
        self.queryset = self.queryset.filter(owner=self.request.user)

