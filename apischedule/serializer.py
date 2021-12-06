from django.db.models import fields
from rest_framework import serializers

from apischedule.models import RouteSchema


class RouteSchemaSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = RouteSchema
        