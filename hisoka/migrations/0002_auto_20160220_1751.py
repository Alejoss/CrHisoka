# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feralspirit',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='feralspirit',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
    ]
