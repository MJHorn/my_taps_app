# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taplists', '0010_auto_20160409_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='broadstyle',
            field=models.CharField(default=b'Shiraz', max_length=200),
        ),
    ]
