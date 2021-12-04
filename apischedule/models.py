from django.db import models


class RouteSchemaManager(models.Manager):
    pass

class RouteSchema(models.Model):

    api_id = models.BigAutoField(primary_key=True,verbose_name="API-ID")
    origin_url = models.CharField(max_length=255, null=False, verbose_name="原始url")
    apigw_url = models.CharField(max_length=255,null=False, verbose_name="在apigw的url")
    from_sys = models.CharField(max_length=128, null=False, verbose_name="源系统")
    name = models.CharField(max_length=128, null=False, verbose_name="api名")

    objects = RouteSchemaManager()
