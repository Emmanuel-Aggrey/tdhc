from django.contrib import admin

# Register your models here.
from literals.models import Group, Status, Location


admin.site.site_header = "THE DEVINE HEALERS CHURCH ADMINISTRATOR"
admin.site.site_title = "THE DEVINE HEALERS CHURCH PORTAL"
admin.site.index_title = "WELCOME THE DEVINE HEALERS CHURCH ADMINISTRATOR PORTAL"

admin.site.register([Group, Status, Location])
