# coding=utf-8
import json
import os

from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.files.uploadedfile import InMemoryUploadedFile

from tagging.models import Tag

from hisoka.models import Fireball, FeralSpirit, GrupoMagicPy
from hisoka.forms import FormCrearFeralSpirit, FormCrearFireball, FormNuevaCarta, FormNuevoGrupo


class HisokasMain(ListView):
    template_name = "hisoka/hisoka_main.html"
    queryset = Fireball.objects.all()
    context_object_name = "fireballs"


class FireballDetail(ListView):
    template_name = "hisoka/fireball_detail.html"
    context_object_name = "feral_spirits"

    def get_queryset(self, *args, **kwargs):
        # el queryset puede ser 'contador' o 'ultima_publicacion'
        if self.kwargs['queryset'] == "contador":
            queryset = FeralSpirit.objects.filter(fireball__slug=self.kwargs['slug_fireball']).order_by('-contador')

        else:
            queryset = FeralSpirit.objects.filter(fireball__slug=self.kwargs['slug_fireball'])

        return queryset

    def get_context_data(self, *args, **kwargs):

        context = super(FireballDetail, self).get_context_data(**kwargs)
        fireball = Fireball.objects.get(slug=self.kwargs['slug_fireball'])
        tags = Tag.objects.all()
        tags_list = [tag.name for tag in tags]
        context['fireball'] = fireball
        context['tags_list'] = json.dumps(tags_list)
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
        return context

    def get_success_url(self, *args, **kwargs):
        fireball = Fireball.objects.get(slug=self.kwargs['slug_fireball'])
        success_url = reverse_lazy('fireball',
                                   kwargs={'slug_fireball': fireball.slug, 'queryset': 'ultima_publicacion'})

        return success_url


def editar_feral(request):

    if request.is_ajax():
        id_feral = request.POST.get('id_feral')
        nombre = request.POST.get('nombre_feral')
        url_feral = request.POST.get('url_feral')

        tags_json = request.POST.get('tags_list')
        python_tags_list = json.loads(tags_json)
        tags_string = " ".join(python_tags_list)

        feral_spirit = get_object_or_404(FeralSpirit, id=id_feral)
        feral_spirit.nombre = nombre
        feral_spirit.url = url_feral
        feral_spirit.save()

        Tag.objects.update_tags(feral_spirit, tags_string)

        return HttpResponse("feral editado", status=204)

    else:
        return HttpResponse(status=400)


def feral_data(request):
    """
    Recibe un feral_id y devuelve los datos de ese feral para llenarlo en el modal
    """
    if request.is_ajax():

        feral_id = request.GET.get('feral_id', '')
        if feral_id:
            feral_spirit = get_object_or_404(FeralSpirit, id=feral_id)
            feral_tags = [tag.name for tag in feral_spirit.tags]
            feral_dict = {'nombre': feral_spirit.nombre, 'url': feral_spirit.url, 'tags': feral_tags,
                          'id': feral_spirit.id}
            feral_response = json.dumps(feral_dict)

            return HttpResponse(feral_response, status=200)

        else:
            return HttpResponse(status=400)

    else:
        return HttpResponse(status=400)


def probar_tweeter(request):
    """
    Prueba el API, a ver si se envian correctamente las imágenes en un tweet
    """

    import tweepy
    fireball_orilla = Fireball.objects.get(nombre="OrillaLibertaria")
    # Envia tweets de Orilla Libertaria a twitter
    access_token_twitter = "1884663464-cKUFhmqTVbEvxbkdOD0rBo1UyXwX20ZrbtseIQc"
    access_token_twitter_secret = os.environ['ACCESS_TOKEN_TWITTER_SECRET']
    consumer_key = "XwIbq6Zwl5rUYzIMheFwx9MXO"
    consumer_secret = os.environ['CONSUMER_SECRET_TWITTER']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_twitter, access_token_twitter_secret)
    api = tweepy.API(auth)

    feral_elegido = FeralSpirit.objects.filter(activo=True, eliminado=False,
                                               fireball=fireball_orilla, tipo="imagen").first()

    filename = feral_elegido.imagen.file.name
    media_ids = api.media_upload(filename=filename)

    params = {'status': 'Las fronteras:', 'media_ids': [media_ids.media_id_string]}
    response = api.update_status(**params)

    print response
    return HttpResponse("Ni te siente!")


# Magic
class MagicPy(TemplateView):

    template_name = "hisoka/magic_py.html"

    def get_context_data(self, **kwargs):

        context = super(MagicPy, self).get_context_data()
        grupos_magicpy = GrupoMagicPy.objects.all()
        context['grupos_magicpy'] = grupos_magicpy
        return context


class NuevaCarta(CreateView):
    template_name = "hisoka/nueva_carta.html"

    form_class = FormNuevaCarta

    success_url = reverse_lazy('hisokas_main')  # Cambiar


class NuevoGrupo(CreateView):
    template_name = "hisoka/nuevo_grupo.html"

    form_class = FormNuevoGrupo

    success_url = reverse_lazy('hisokas_main')  # Cambiar
