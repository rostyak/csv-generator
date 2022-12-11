from django.contrib import admin

from csv_data_work.models import Schema


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    pass
