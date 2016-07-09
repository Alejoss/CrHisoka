# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0006_auto_20160708_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartamagicpy',
            name='nombre_carta_magic',
            field=models.CharField(unique=True, max_length=255, blank=True),
        ),
    ]
