# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hisoka.models


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0002_auto_20160706_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartamagicpy',
            name='imagen_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='cartamagicpy',
            name='imagen',
            field=models.ImageField(null=True, upload_to=hisoka.models.ubicar_magicpy),
        ),
    ]
