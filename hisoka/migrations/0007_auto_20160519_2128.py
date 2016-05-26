# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0006_auto_20160519_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartamagicpy',
            name='grupo',
            field=models.ForeignKey(to='hisoka.GrupoMagicPy', null=True),
        ),
    ]
