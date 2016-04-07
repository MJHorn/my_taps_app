# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taplists', '0003_auto_20160405_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('style',),
            },
        ),
        migrations.AddField(
            model_name='tap',
            name='beerurl',
            field=models.CharField(default=b'https://untappd.com/b/the-alchemist-heady-topper/4691', max_length=200),
        ),
        migrations.AddField(
            model_name='tap',
            name='style',
            field=models.ManyToManyField(to='taplists.Style'),
        ),
    ]