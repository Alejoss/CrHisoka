# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hisoka.models


class Migration(migrations.Migration):

    dependencies = [
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
                ('imagen', models.URLField(blank=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('descripcion', models.CharField(max_length=600, blank=True)),
                ('ultima_revision', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeralSpirit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=60)),
                ('texto', models.CharField(max_length=150)),
                ('url', models.URLField(blank=True)),
                ('imagen', models.ImageField(null=True, upload_to=hisoka.models.ubicar_imagen_feral, blank=True)),
                ('tema', models.CharField(max_length=150, blank=True)),
                ('contador', models.PositiveIntegerField(default=0)),
                ('ultima_publicacion', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-ultima_publicacion'],
            },
        ),
        migrations.CreateModel(
            name='Fireball',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=150, blank=True)),
                ('nombre', models.CharField(max_length=150)),
                ('url_amazon', models.CharField(max_length=150, blank=True)),
                ('twitter', models.CharField(max_length=150, blank=True)),
                ('imagen', models.URLField(null=True, blank=True)),
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
            model_name='feralspirit',
            name='fireball',
            field=models.ForeignKey(to='hisoka.Fireball'),
        ),
        migrations.AddField(
            model_name='cartamagicpy',
            name='grupo',
            field=models.ForeignKey(to='hisoka.GrupoMagicPy', null=True),
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
