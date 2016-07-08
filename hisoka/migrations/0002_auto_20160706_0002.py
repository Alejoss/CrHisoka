# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feralspirit',
            name='texto',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='grupomagicpy',
            name='imagen',
            field=models.URLField(blank=True),
        ),
    ]
