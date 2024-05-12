from django.contrib import admin

# Register your models here.
from literals.models import Group, Status, Location


admin.site.register([Group, Status, Location])
