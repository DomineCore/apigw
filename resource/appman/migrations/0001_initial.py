# Generated by Django 3.2.9 on 2021-12-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppMan',
            fields=[
                ('app_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='APPID')),
                ('app_sk', models.CharField(max_length=255, verbose_name='应用密钥')),
                ('name', models.CharField(max_length=255, verbose_name='应用名')),
                ('host', models.CharField(max_length=255, verbose_name='应用HOST')),
            ],
            options={
                'verbose_name': '应用管理',
            },
        ),
    ]