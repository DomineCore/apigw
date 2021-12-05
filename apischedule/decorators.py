from functools import wraps

from rest_framework.response import Response

from apischedule.models import RouteSchema
from resource.app.models import App
from apigw.core.response import ResponseApi404

def path_validator(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # check param
        path = request.path
        appid = path.split('/')[0]
        apigw_url = '/' + path.lstrip(appid).lstrip('/')
        app = App.objects.get_app(appid)
        route = RouteSchema.objects.get_url(apigw_url,appid)
        if not app:
            return ResponseApi404(appid)
        if not route:
            return ResponseApi404(path)
        return func(request, app, route, *args, **kwargs)
    return wrapper
