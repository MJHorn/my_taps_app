# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taplists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barname', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('barname',),
            },
        ),
        migrations.RemoveField(
            model_name='tap',
            name='bar',
        ),
        migrations.AlterField(
            model_name='tap',
            name='rating',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AddField(
            model_name='tap',
            name='bar',
            field=models.ManyToManyField(to='taplists.Bar'),
        ),
    ]
