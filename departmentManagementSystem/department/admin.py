from django.contrib import admin
from .models import Department

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_code', 'head_of_department','department_description', 'status','contact_email','contact_phone_number','department_location','created_at', 'created_by')
    search_fields = ('department_name', 'department_code', 'head_of_department')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)