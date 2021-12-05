from django.db import models


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
    create_time = models.DateTimeField(auto_created=True)

    objects = ApiSentryManager()
