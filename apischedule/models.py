from django.db import models


class RouteSchemaManager(models.Manager):
    def get_url(self,apigw_url,from_sys):
        route = self.filter(from_sys=from_sys,apigw_url=apigw_url).first()
        return route

class RouteSchema(models.Model):
    api_id = models.BigAutoField(primary_key=True,verbose_name="API-ID")
    origin_url = models.CharField(max_length=255, null=False, verbose_name="原始url")
    apigw_url = models.CharField(max_length=255,null=False, verbose_name="在apigw的url")
    from_sys = models.IntegerField(null=False, verbose_name="所属应用")
    name = models.CharField(max_length=128, null=False, verbose_name="api名")

    objects = RouteSchemaManager()

    class Meta:
        unique_together = ("from_sys","apigw_url")
        verbose_name = "网关路由表"

