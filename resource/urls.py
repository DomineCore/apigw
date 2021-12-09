from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from resource.appman.viewset import AppManViewSet
from apischedule.viewset import RouteSchemaViewSet
from requestrec.viewset import RequestRecViewSet
from resource.apisentry.viewset import ApiSentryViewSet

v1_api_router = DefaultRouter()

v1_api_router.register('app',AppManViewSet,"app")
v1_api_router.register('apiresource',RouteSchemaViewSet,'apiresource')
v1_api_router.register('requestrec',RequestRecViewSet,'requestrec')
v1_api_router.register('apisentry',ApiSentryViewSet,'apisentry')
