# coding=utf-8
import json
import os

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.decorators.csrf import csrf_exempt

from tagging.models import Tag

from hisoka.models import Fireball, FeralSpirit, GrupoMagicPy
from hisoka.forms import FormCrearFeralSpirit, FormCrearFireball, FormNuevaCarta, FormNuevoGrupo, MultipleImagesFeral


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
            queryset = FeralSpirit.objects.filter(fireball__slug=self.kwargs['slug_fireball'], eliminado=False).order_by('-contador')

        else:
            queryset = FeralSpirit.objects.filter(fireball__slug=self.kwargs['slug_fireball'], eliminado=False)

        return queryset

    def get_context_data(self, *args, **kwargs):

        context = super(FireballDetail, self).get_context_data(**kwargs)
        fireball = Fireball.objects.get(slug=self.kwargs['slug_fireball'])
        filtro = self.kwargs['queryset']
        tags = Tag.objects.all()
        tags_list = [tag.name for tag in tags]
        context['fireball'] = fireball
        context['filtro'] = filtro
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
        tipo_feral = self.kwargs['tipo_feral']

        context['fireball'] = fireball
        context['tipo_feral'] = tipo_feral
        return context

    def get_success_url(self, *args, **kwargs):
        fireball = Fireball.objects.get(slug=self.kwargs['slug_fireball'])
        success_url = reverse_lazy('fireball',
                                   kwargs={'slug_fireball': fireball.slug, 'queryset': 'ultima_publicacion'})

        return success_url


def multiple_images(request, slug_fireball):
    # Maneja un formulario con la opcion de subir varias imágenes a la ves
    template = "hisoka/multiple_images.html"
    fireball = Fireball.objects.get(slug=slug_fireball)

    if request.method == "POST":
        files = request.FILES.getlist('images')
        for x in files:
            FeralSpirit.objects.create(tipo="imagen", imagen=x, fireball=fireball)
        return HttpResponse('Proceso las files')

    context = {'fireball': fireball}
    return render(request, template, context)


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
            feral_dict = {'texto': feral_spirit.texto, 'url': feral_spirit.url, 'tags': feral_tags,
                          'id': feral_spirit.id, 'tipo': feral_spirit.tipo}
            feral_response = json.dumps(feral_dict)

            return HttpResponse(feral_response, status=200)

        else:
            return HttpResponse(status=400)

    else:
        return HttpResponse(status=400)


def eliminar_feral(request):
    """
    recibe un feral_id y elimina el objeto FeralSpirit correspondiente
    """
    if request.is_ajax():
        feral_id = request.POST.get('feral_id', '')
        if feral_id:
            feral_spirit = get_object_or_404(FeralSpirit, id=feral_id)
            feral_spirit.eliminado = True
            feral_spirit.save()
            return HttpResponse("Feral correctamente eliminado")
        else:
            return HttpResponse("No hay feral_id",status=400)
    else:
        return HttpResponse("No es Ajax", status=400)


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
