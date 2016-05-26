# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hisoka.models


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0007_auto_20160519_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='feralspirit',
            name='imagen',
            field=models.ImageField(null=True, upload_to=hisoka.models.ubicar_imagen_feral),
        ),
    ]
