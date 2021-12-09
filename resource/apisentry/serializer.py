from django.db.models import fields
from rest_framework import serializers

from resource.apisentry.models import ApiSentry

class ApiSentrySerializer(serializers.ModelSerializer):
    
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    class Meta:
        fields = "__all__"
        model = ApiSentry
