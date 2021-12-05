from django.db import models


class AppManager(models.Manager):
    def get_app(self,appid):
        app = self.filter(app_id=appid).first()
        return app

class AppMan(models.Model):

    app_id = models.BigAutoField(primary_key=True,verbose_name="APPID")
    app_sk = models.CharField(max_length=255,null=False,verbose_name="应用密钥")
    name = models.CharField(max_length=255,verbose_name="应用名")
    host = models.CharField(max_length=255,verbose_name="应用HOST")

    objects = AppManager()

    class Meta:
        verbose_name = "应用管理"
