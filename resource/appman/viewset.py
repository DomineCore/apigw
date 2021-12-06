from rest_framework.viewsets import ModelViewSet

from resource.appman.serializers import AppManSerializer
from resource.appman.models import AppMan

class AppManViewSet(ModelViewSet):

    serializer_class = AppManSerializer
    queryset = AppMan.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
