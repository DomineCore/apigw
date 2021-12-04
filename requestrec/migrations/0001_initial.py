# Generated by Django 3.2.9 on 2021-12-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestRec',
            fields=[
                ('request_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='请求ID')),
                ('request_sys', models.CharField(max_length=255, verbose_name='请求来源系统')),
                ('response_sys', models.CharField(max_length=255, verbose_name='请求目标系统')),
                ('request_message', models.TextField(verbose_name='请求消息')),
                ('response_message', models.TextField(verbose_name='响应消息')),
                ('request_time', models.DateTimeField(verbose_name='请求时间')),
                ('request_api_id', models.IntegerField(verbose_name='apiID')),
            ],
        ),
    ]