# Generated by Django 3.2.9 on 2021-12-09 14:23

import apigw.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apisentry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apisentry',
            name='create_time',
            field=apigw.models.fields.CustomDateTimeField(auto_created=True, auto_now=True),
        ),
    ]
