from rest_framework import serializers

from requestrec.models import RequestRec

class RequestRecSerializer(serializers.ModelSerializer):

    request_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    class Meta:
        fields = "__all__"
        model = RequestRec
