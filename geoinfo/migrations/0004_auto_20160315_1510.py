# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-15 15:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoinfo', '0003_auto_20160218_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='polygon',
            name='claims',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polygon',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
