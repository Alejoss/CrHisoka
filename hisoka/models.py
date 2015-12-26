from django.db import models
from django.template.defaultfilters import slugify


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
	contador = models.PositiveIntegerField(default=0)
	ultima_publicacion = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %s " % (self.nombre, self.tipo)

	class Meta:
		ordering = ['-ultima_publicacion']
