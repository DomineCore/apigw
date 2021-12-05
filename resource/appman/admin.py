from django.contrib import admin
from django.contrib.admin import ModelAdmin

from resource.appman.models import AppMan

class AppManAdmin(ModelAdmin):
    list_display = [
        "app_id",
        "app_sk",
        "name",
        "host"
    ]

admin.site.register(AppMan, AppManAdmin)
