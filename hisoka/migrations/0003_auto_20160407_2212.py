# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0002_auto_20160220_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaminoMagicPy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prioridad', models.PositiveSmallIntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='CartaMagicPy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'')),
                ('grupo', models.CharField(max_length=150, blank=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('descripcion', models.CharField(max_length=600, blank=True)),
                ('ultima_revision', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoMagicPy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150, blank=True)),
                ('descripcion', models.CharField(max_length=600, blank=True)),
                ('imagen', models.ImageField(upload_to=b'')),
                ('ultima_revision', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='caminomagicpy',
            name='primera_carta',
            field=models.ForeignKey(related_name='primera_carta', to='hisoka.CartaMagicPy'),
        ),
        migrations.AddField(
            model_name='caminomagicpy',
            name='segunda_carta',
            field=models.ForeignKey(related_name='segunda_carta', to='hisoka.CartaMagicPy'),
        ),
    ]
