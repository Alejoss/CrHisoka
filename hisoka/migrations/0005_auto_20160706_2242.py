# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0004_cartamagicpy_nombre_carta_magic'),
    ]

    operations = [
        migrations.AddField(
            model_name='caminomagicpy',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartamagicpy',
            name='eliminada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='grupomagicpy',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
    ]
