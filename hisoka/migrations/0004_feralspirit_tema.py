# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0003_auto_20160407_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='feralspirit',
            name='tema',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
