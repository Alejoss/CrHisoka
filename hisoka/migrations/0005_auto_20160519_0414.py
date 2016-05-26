# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hisoka.models


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0004_feralspirit_tema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartamagicpy',
            name='imagen',
            field=models.ImageField(upload_to=hisoka.models.ubicar_imagen_magicpy),
        ),
        migrations.AlterField(
            model_name='feralspirit',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='fireball',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
