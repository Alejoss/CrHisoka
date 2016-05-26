# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0005_auto_20160519_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartamagicpy',
            name='imagen',
            field=models.URLField(blank=True),
        ),
    ]
