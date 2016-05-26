# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hisoka.models


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0008_feralspirit_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feralspirit',
            old_name='nombre',
            new_name='texto',
        ),
        migrations.AlterField(
            model_name='feralspirit',
            name='imagen',
            field=models.ImageField(null=True, upload_to=hisoka.models.ubicar_imagen_feral, blank=True),
        ),
    ]
