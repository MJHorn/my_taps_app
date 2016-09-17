# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bar', models.CharField(default=b'FinshnPig', max_length=200)),
                ('region', models.CharField(default=b'Farmville', max_length=200)),
                ('state', models.CharField(default=b'NY', max_length=200)),
            ],
            options={
                'ordering': ('bar', 'region'),
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('style', models.CharField(max_length=200)),
                ('broadstyle', models.CharField(default=b'Shiraz', max_length=200)),
            ],
            options={
                'ordering': ('style',),
            },
        ),
        migrations.CreateModel(
            name='Tap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brewery', models.CharField(max_length=200)),
                ('beer', models.CharField(max_length=200)),
                ('rating', models.DecimalField(max_digits=5, decimal_places=3)),
                ('beerurl', models.CharField(default=b'https://untappd.com/b/the-alchemist-heady-topper/4691', max_length=200)),
                ('image', models.CharField(default=b'http://vignette3.wikia.nocookie.net/pokemon/images/1/16/025Pikachu_OS_anime_10.png/revision/20150102074354', max_length=200)),
                ('abv', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
                ('ibu', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
                ('state', models.CharField(default=b'NY', max_length=200)),
                ('bar', models.ManyToManyField(default=b'FinshnPig', to='taplists.Bar')),
                ('style', models.ManyToManyField(to='taplists.Style')),
            ],
        ),
    ]
