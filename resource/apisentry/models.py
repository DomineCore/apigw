from django.db import models
from apigw.models.fields import CustomDateTimeField

class ApiSentryManager(models.Manager):
    def save_trace(self,trace_msg,api,sys):
        trace = self.create(
            trace_msg=trace_msg,
            api=api,
            sys=sys
        )
        trace.save()
        return trace

class ApiSentry(models.Model):
    
    trace_msg = models.TextField(verbose_name="异常信息")
    api = models.IntegerField(verbose_name="api-id")
    sys = models.IntegerField(verbose_name="appid")
    create_time = CustomDateTimeField(auto_created=True,auto_now=True)

    objects = ApiSentryManager()
