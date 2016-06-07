# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taplists', '0014_tap_ibu'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='state',
            field=models.CharField(default=b'NY', max_length=200),
        ),
        migrations.AddField(
            model_name='tap',
            name='state',
            field=models.CharField(default=b'NY', max_length=200),
        ),
    ]
