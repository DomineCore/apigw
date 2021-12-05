from django.conf.urls import url

from apischedule.views.api_bouncer import api_bouncer

apigwpatterns = [
    url('apigw/(?P<app_id>\w+)/(?P<apigw_url>\w+)/', api_bouncer)
]
