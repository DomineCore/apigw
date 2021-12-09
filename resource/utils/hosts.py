from django.conf import settings

from resource.appman.models import AppMan
from apischedule.models import RouteSchema

APIGW_ROOT_URL = settings.APIGW_ROOT_URL


def get_realurls_by_app_id(app_id):
    url_dict = RouteSchema.objects.get_url_dict_by_appid(app_id)
    # build real url
    app = AppMan.objects.filter(app_id=app_id).first()
    if not app:
        return {}
    host = app.host
    for key in url_dict.keys():
        url_dict[key] = host.rstrip('/') + '/' + str(url_dict[key]).lstrip('/')
    # {api_id:real_url}
    return url_dict

def build_link(apigw_url,app_id):
    return APIGW_ROOT_URL + str(app_id) + '/' + apigw_url.strip('/') + '/'