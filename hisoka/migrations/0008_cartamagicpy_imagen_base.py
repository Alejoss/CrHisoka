# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hisoka.models


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0007_auto_20160709_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartamagicpy',
            name='imagen_base',
            field=models.ImageField(null=True, upload_to=hisoka.models.ubicar_img_base),
        ),
    ]
