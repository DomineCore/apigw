from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from apischedule.models import RouteSchema
from apischedule.serializer import RouteSchemaSerializer


class RouteSchemaViewSet(ModelViewSet):

    queryset = RouteSchema.objects.all()
    serializer_class = RouteSchemaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["from_sys"]
