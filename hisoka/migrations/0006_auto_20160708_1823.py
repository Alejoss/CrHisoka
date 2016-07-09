# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hisoka', '0005_auto_20160706_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartaConjunto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ConjuntoCartas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=600, blank=True)),
                ('descripcion', models.CharField(max_length=600, blank=True)),
                ('eliminado', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('ultima_revision', models.DateTimeField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='caminomagicpy',
            name='primera_carta',
        ),
        migrations.RemoveField(
            model_name='caminomagicpy',
            name='segunda_carta',
        ),
        migrations.AlterModelOptions(
            name='cartamagicpy',
            options={'ordering': ['-ultima_revision']},
        ),
        migrations.DeleteModel(
            name='CaminoMagicPy',
        ),
        migrations.AddField(
            model_name='cartaconjunto',
            name='carta',
            field=models.ForeignKey(to='hisoka.CartaMagicPy'),
        ),
        migrations.AddField(
            model_name='cartaconjunto',
            name='conjunto',
            field=models.ForeignKey(to='hisoka.ConjuntoCartas'),
        ),
    ]
