from functools import wraps

from rest_framework.response import Response

from apischedule.models import RouteSchema
from resource.appman.models import AppMan
from apigw.core.response import ResponseApi404

def path_validator(func):
    @wraps(func)
    def wrapper(request, app_id, apigw_url, *args, **kwargs):
        # check param
        if not app_id:
            return ResponseApi404(app_id)
        if not apigw_url:
            return ResponseApi404(app_id + '/' + apigw_url)
        app = AppMan.objects.get_app(app_id)
        route = RouteSchema.objects.get_url(apigw_url,app_id)
        if not app:
            return ResponseApi404(app_id)
        if not route:
            return ResponseApi404(app_id + '/' + apigw_url)
        return func(request, app, route, *args, **kwargs)
    return wrapper
