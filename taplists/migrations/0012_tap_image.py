# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taplists', '0011_style_broadstyle'),
    ]

    operations = [
        migrations.AddField(
            model_name='tap',
            name='image',
            field=models.CharField(default=b'http://vignette3.wikia.nocookie.net/pokemon/images/1/16/025Pikachu_OS_anime_10.png/revision/20150102074354', max_length=200),
        ),
    ]
