from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from csv_data_work.models import Schema


def index(request):
    return render(request, "csv_data_work/index.html")


class SchemaListView(LoginRequiredMixin, generic.ListView):
    model = Schema
    queryset = Schema.objects.all()
    template_name = "csv_data_work/schema_list.html"
    context_object_name = "schema_list"


class SchemaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Schema
    fields = "__all__"
    success_url = reverse_lazy("csv_data_work:schema-list")
    template_name = "csv_data_work/schema_form.html"


class SchemaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Schema
    fields = "__all__"
    success_url = reverse_lazy("csv_data_work:schema-list")
    template_name = "csv_data_work/schema_form.html"


