from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Person

# Register your models here.

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ['name', 'nat_id', 'birth_date','seri_no']
    search_fields = ['name', 'nat_id']
    list_filter = ['created_date']