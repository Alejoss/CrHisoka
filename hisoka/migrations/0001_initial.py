# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeralSpirit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=150)),
                ('url', models.URLField()),
                ('contador', models.PositiveIntegerField(default=0)),
                ('ultima_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-ultima_publicacion'],
            },
        ),
        migrations.CreateModel(
            name='Fireball',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=150, blank=True)),
                ('nombre', models.CharField(max_length=150)),
                ('url_amazon', models.CharField(max_length=150, blank=True)),
                ('twitter', models.CharField(max_length=150, blank=True)),
                ('imagen', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='feralspirit',
            name='fireball',
            field=models.ForeignKey(to='hisoka.Fireball'),
        ),
    ]
