from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from apischedule.models import RouteSchema
from apischedule.serializer import RouteSchemaSerializer
from resource.utils.hosts import build_link

class RouteSchemaViewSet(ModelViewSet):

    queryset = RouteSchema.objects.all()
    serializer_class = RouteSchemaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["from_sys"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        app_id = request.GET.get('from_sys')
        serializer = self.get_serializer(queryset, many=True)
        url_datas = serializer.data
        # 查询所有app的host
        if app_id:
            # url重组
            for url in url_datas:
                url['apigw_url'] = build_link(url['apigw_url'], url['from_sys'])
        return Response(data=url_datas)
