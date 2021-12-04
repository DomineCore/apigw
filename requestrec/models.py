from django.db import models


class RequestRecManager(models.Manager):
    pass


class RequestRec(models.Model):

    request_id = models.BigAutoField(primary_key=True,verbose_name="请求ID")
    request_sys = models.CharField(max_length=255, null=False, verbose_name="请求来源系统")
    response_sys = models.CharField(max_length=255, null=False, verbose_name="请求目标系统")
    request_message = models.TextField(verbose_name="请求消息")
    response_message = models.TextField(verbose_name="响应消息")
    request_time = models.DateTimeField(verbose_name="请求时间")
    request_api_id = models.IntegerField(verbose_name="apiID")
    
    objects = RequestRecManager()
