from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from apigw.pagination import ApigwLimitOffPagination
from requestrec.models import RequestRec
from requestrec.serializer import RequestRecSerializer
from apischedule.models import RouteSchema


class RequestRecViewSet(ModelViewSet):
    queryset = RequestRec.objects.all().order_by("-request_time")
    serializer_class = RequestRecSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["response_sys"]
    pagination_class = ApigwLimitOffPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        serializer = self.get_serializer(page if page is not None else queryset, many=True)
        datas = serializer.data
        # 获取所有api_id
        api_id_list = set([
            data["api"]
            for data in datas
        ])
        # 查询api-name dict
        api_dict = dict(
            RouteSchema.objects
            .filter(api_id__in=api_id_list)
            .values_list("api_id","name")
        )
        # build name
        for data in datas:
            data["name"] = api_dict.get(data["api"], str(data["api"])+"(name未知)")

        
        return (
            self.get_paginated_response(datas)
            if page is not None
            else Response(datas)
        )

