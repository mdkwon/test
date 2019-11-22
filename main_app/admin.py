from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Make, Year, CarModel, Engine

@admin.register(Make, Year, CarModel, Engine)
class ViewAdmin(ImportExportModelAdmin):
    pass