from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apischedule.models import RouteSchema

class ApiScheduleAdmin(ModelAdmin):
    list_display = (
        'api_id',
        'origin_url',
        'apigw_url',
        'from_sys',
        'name'
    )

admin.site.register(RouteSchema, ApiScheduleAdmin)

