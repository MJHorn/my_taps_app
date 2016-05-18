# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taplists', '0012_tap_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tap',
            name='abv',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=1),
        ),
    ]
