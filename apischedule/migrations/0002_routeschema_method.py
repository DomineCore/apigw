# Generated by Django 3.2.9 on 2021-12-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apischedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='routeschema',
            name='method',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST')], default='GET', max_length=10, verbose_name='请求方法'),
        ),
    ]