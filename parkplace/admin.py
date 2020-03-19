from django.contrib import admin
from .models import *

admin.site.register(Place)
admin.site.register(Reserves)
# Register your models here.

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['device_name', 'x_coordinate', 'y_coordinate', 'z_coordinate']

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['device_name', 'x_coordinate', 'y_coordinate', 'z_coordinate']