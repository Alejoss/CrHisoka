# coding=utf-8
from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from tagging.registry import register as register_tag
from storages.backends.s3boto import S3BotoStorage


class Fireball(models.Model):
    slug = models.SlugField(max_length=150, blank=True)
    nombre = models.CharField(max_length=150)
    url_amazon = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    imagen = models.URLField(blank=True)

    def get_absolute_url():
        pass

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)

        return super(Fireball, self).save(*args, **kwargs)


class FeralSpirit(models.Model):
    fireball = models.ForeignKey(Fireball)
    tipo = models.CharField(max_length=60)
    nombre = models.CharField(max_length=150)
    url = models.URLField()
    tema = models.CharField(max_length=150, blank=True)
    contador = models.PositiveIntegerField(default=0)
    ultima_publicacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)  # Solo los ferals activos se twitean
    eliminado = models.BooleanField(default=False)  # los ferals eliminados no salen en contenido_extra

    def aumentar_contador(self):
        self.contador += 1
        self.save()
        return self.contador

    def __unicode__(self):
        return "%s : %s " % (self.nombre, self.tipo)

    class Meta:
        ordering = ['-ultima_publicacion']


register_tag(FeralSpirit)


# Magic  !!! Falta definir donde se guardan las imagenes

class GrupoMagicPy(models.Model):

    nombre = models.CharField(max_length=150, blank=True)
    descripcion = models.CharField(max_length=600, blank=True)
    imagen = models.ImageField(upload_to="")
    ultima_revision = models.DateTimeField(null=True)

    @property
    def hace_cuanto_revise(self):
        # Devuelve un texto con la diferencia de hoy a la ultima revision

        diferencia_tiempo = datetime.today() - self.ultima_revision

        dias = diferencia_tiempo.days

        if dias == 0:
            return "Hoy"

        meses = float(dias)/30.00
        if meses > 0:
            return "%s meses - %s dias" % (meses, dias % 30)

        else:
            return "%s dias" % dias


def ubicar_imagen_magicpy(instance):
    path = "/".join([instance.grupo, instance.nombre])
    return path


class CartaMagicPy(models.Model):
    """
    Una carta con idea guardada
    """
    imagen = models.ImageField(upload_to=ubicar_imagen_magicpy,
                               storage=S3BotoStorage(bucket='magic_py'))
    grupo = models.CharField(max_length=150, blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length= 600, blank=True)

    ultima_revision = models.DateTimeField(null=True)

    @property
    def hace_cuanto_revise(self):
        # Devuelve un texto con la diferencia de hoy a la ultima revision

        diferencia_tiempo = datetime.today() - self.ultima_revision

        dias = diferencia_tiempo.days

        if dias == 0:
            return "Hoy"

        meses = float(dias)/30.00
        if meses > 0:
            return "%s meses - %s dias" % (meses, dias % 30)

        else:
            return "%s dias" % dias


    def __unicode__(self):
        return self.nombre


class CaminoMagicPy(models.Model):

    primera_carta = models.ForeignKey(CartaMagicPy, related_name="primera_carta")
    segunda_carta = models.ForeignKey(CartaMagicPy, related_name="segunda_carta")
    prioridad = models.PositiveSmallIntegerField(default=2)  # Prioridad del 1 al 3
