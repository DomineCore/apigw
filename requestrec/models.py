from django.db import models


class RequestRecManager(models.Manager):
    def save_req_resp(self, kwargs):
        request_rec = self.create(**kwargs)
        request_rec.save()
        return request_rec

class RequestRec(models.Model):

    request_id = models.BigAutoField(primary_key=True,verbose_name="请求ID")
    request_sys = models.CharField(max_length=255, null=False, verbose_name="请求来源系统")
    response_sys = models.CharField(max_length=255, null=False, verbose_name="请求目标系统")
    method = models.CharField(max_length=10,verbose_name="请求方法",null=False)
    request_message = models.TextField(verbose_name="请求消息")
    response_message = models.TextField(verbose_name="响应消息")
    request_time = models.DateTimeField(verbose_name="请求时间",auto_created=True)
    api = models.IntegerField(verbose_name="请求的api")
    
    objects = RequestRecManager()
