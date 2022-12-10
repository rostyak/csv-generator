from django.shortcuts import render


def index(request):
    return render(request, "csv_data_work/index.html")
