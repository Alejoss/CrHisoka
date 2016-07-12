# coding=utf-8
from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from tagging.registry import register as register_tag
from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


class Fireball(models.Model):
    slug = models.SlugField(max_length=150, blank=True)
    nombre = models.CharField(max_length=150)
    url_amazon = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    imagen = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)

        return super(Fireball, self).save(*args, **kwargs)


def ubicar_imagen_feral(instance, filename):
    # Para ubicar las imágenes de feralspirits str(instance.ultimo_id() + 1
    path = "/".join([instance.fireball.nombre, filename])
    return path


class FeralSpirit(models.Model):
    # , storage=S3BotoStorage(bucket='criptolibertad')
    fireball = models.ForeignKey(Fireball)
    tipo = models.CharField(max_length=60)
    texto = models.CharField(max_length=150, blank=True)
    url = models.URLField(blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to=ubicar_imagen_feral, storage=S3BotoStorage(bucket=settings.AWS_STORAGE_BUCKET_NAME))
    tema = models.CharField(max_length=150, blank=True)
    contador = models.PositiveIntegerField(default=0)
    ultima_publicacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)  # Solo los ferals activos se twitean
    eliminado = models.BooleanField(default=False)  # los ferals eliminados no salen en contenido_extra

    def aumentar_contador(self):
        self.contador += 1
        self.save()
        return self.contador

    @classmethod
    def ultimo_id(cls):
        # para obtener el id del ultimo feral creado, para nombrar los archivos en el storage
        ultimo_feral = cls.objects.filter(eliminado=False).latest('id')
        return ultimo_feral.id

    def __unicode__(self):
        return "%s : %s " % (self.fireball.nombre, self.tipo)

    class Meta:
        ordering = ['-ultima_publicacion']


register_tag(FeralSpirit)


def ubicar_imagen_magicpy(instance, filename):
    path = "/".join(["grupos_magicpy", filename])
    return path


# Magic
class GrupoMagicPy(models.Model):
    nombre = models.CharField(max_length=150, blank=True)
    descripcion = models.CharField(max_length=600, blank=True)
    imagen = models.URLField(blank=True)
    eliminado = models.BooleanField(default=False)
    ultima_revision = models.DateTimeField(null=True)

    @property
    def hace_cuanto_revise(self):
        # Devuelve un texto con la diferencia de hoy a la ultima revision

        diferencia_tiempo = datetime.today() - self.ultima_revision

        dias = diferencia_tiempo.days

        if dias == 0:
            return "Hoy"

        meses = float(dias) / 30.00
        if meses > 0:
            return "%s meses - %s dias" % (meses, dias % 30)

        else:
            return "%s dias" % dias

    def __unicode__(self):
        return self.nombre


def ubicar_magicpy(instance, filename):
    # Para ubicar las imágenes de magicpy
    nombre_archivo = instance.nombre + ".jpeg"
    path = "/".join([instance.grupo.nombre, nombre_archivo])
    return path


def ubicar_img_base(instance, filename):
    # Ubica la imagen base, la que no ha sido recortada
    nombre_archivo = "0_" + instance.nombre + ".jpeg"
    path = "/".join([instance.grupo.nombre, nombre_archivo])
    return path


class CartaMagicPy(models.Model):
    """
    Una carta con idea guardada
    """
    # , storage=S3BotoStorage(bucket=settings.AWS_STORAGE_BUCKET_NAME)
    imagen_url = models.URLField(blank=True)
    nombre_carta_magic = models.CharField(max_length=255, blank=True, unique=True)
    imagen = models.ImageField(null=True, upload_to=ubicar_magicpy, storage=S3BotoStorage(bucket=settings.AWS_STORAGE_BUCKET_NAME))
    imagen_base = models.ImageField(null=True, upload_to=ubicar_img_base, storage=S3BotoStorage(bucket=settings.AWS_STORAGE_BUCKET_NAME))
    grupo = models.ForeignKey(GrupoMagicPy, null=True)
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=600, blank=True)
    ultima_revision = models.DateTimeField(null=True)
    eliminada = models.BooleanField(default=False)

    @property
    def hace_cuanto_revise(self):
        # Devuelve un texto con la diferencia de hoy a la ultima revision

        diferencia_tiempo = datetime.today() - self.ultima_revision

        dias = diferencia_tiempo.days

        if dias == 0:
            return "Hoy"

        meses = float(dias) / 30.00
        if meses > 0:
            return "%s meses - %s dias" % (meses, dias % 30)

        else:
            return "%s dias" % dias

    class Meta:
        ordering = ["-ultima_revision"]

    def __unicode__(self):
        return self.nombre


class ConjuntoCartas(models.Model):
    nombre = models.CharField(max_length=600, blank=True)
    descripcion = models.CharField(max_length=600, blank=True)
    eliminado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(null=True)
    ultima_revision = models.DateTimeField(null=True)


class CartaConjunto(models.Model):
    carta = models.ForeignKey(CartaMagicPy)
    conjunto = models.ForeignKey(ConjuntoCartas)
    eliminado = models.BooleanField(default=False)
