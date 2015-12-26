from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from hisoka.models import Fireball, FeralSpirit
from hisoka.forms import FormCrearFeralSpirit, FormCrearFireball


class HisokasMain(ListView):

	template_name = "hisoka/hisoka_main.html"
	queryset = Fireball.objects.all()
	context_object_name = "fireballs"


class FireballDetail(ListView):

	template_name = "hisoka/fireball_detail.html"
	context_object_name = "feral_spirits"

	def get_queryset(self, *args, **kwargs):

		if self.kwargs['queryset'] == "contador":
			queryset = FeralSpirit.objects.filter(fireball__slug=self.kwargs['slug_fireball']).order_by('-contador')
		else:
			queryset = FeralSpirit.objects.filter(fireball__slug=self.kwargs['slug_fireball'])

		return queryset

	def get_context_data(self, *args, **kwargs):

		context = super(FireballDetail, self).get_context_data(*args, **kwargs)
		fireball = Fireball.objects.get(slug=self.kwargs['slug_fireball'])
		context['fireball'] = fireball
		return context


class CrearFireball(CreateView):

	success_url = reverse_lazy('hisokas_main')
	template_name = "hisoka/crear_fireball.html"
	form_class = FormCrearFireball


class CrearFeralSpirit(CreateView):

	template_name = "hisoka/crear_feral_spirit.html"
	form_class = FormCrearFeralSpirit

	def form_valid(self, form):

		fireball = Fireball.objects.get(slug=self.kwargs.get('slug_fireball'))
		form.instance.fireball = fireball

		return super(CrearFeralSpirit, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(CrearFeralSpirit, self).get_context_data(*args, **kwargs)
		fireball = Fireball.objects.get(slug=self.kwargs['slug_fireball'])

		context['fireball'] = fireball
		print context
		return context

	def get_success_url(self, *args, **kwargs):

		fireball = Fireball.objects.get(slug=self.kwargs['slug_fireball'])
		success_url = reverse_lazy('fireball', kwargs={'slug_fireball': fireball.slug, 'queryset': 'ultima_publicacion'})

		return success_url
