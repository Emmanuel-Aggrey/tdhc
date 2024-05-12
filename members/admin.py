from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from members.models import Member


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'baptismal_date',
                    'digital_address', 'location', 'occupation', 'status', 'marital_status']

    list_editable = ['phone_number', 'status', 'marital_status']

    search_fields = ['first_name', 'last_name', 'phone_number']
    list_filter = ['location', 'baptismal_date', 'marital_status', 'status']
    filter_horizontal = ['group']
