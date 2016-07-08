# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0003_auto_20160706_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartamagicpy',
            name='nombre_carta_magic',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
