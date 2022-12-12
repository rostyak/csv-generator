from django.contrib import admin

from csv_data_work.models import Schema, Column


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    pass


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass
