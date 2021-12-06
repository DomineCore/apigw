from rest_framework import serializers

from resource.appman.models import AppMan

class AppManSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = AppMan
