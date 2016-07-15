# coding=utf-8
import json
import base64
import requests
import bleach
from StringIO import StringIO
from PIL import Image
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.files.base import ContentFile
from django.db.models import Count

from tagging.models import Tag

from hisoka.models import Fireball, FeralSpirit, GrupoMagicPy, CartaMagicPy, ConjuntoCartas, CartaConjunto
from hisoka.forms import FormCrearFeralSpirit, FormCrearFireball, FormNuevaCarta, FormNuevoGrupo


class Prueba(TemplateView):
    # renderea un html sin tanta waa para aislar y probar librerias de frontend
    template_name = "hisoka/prueba.html"


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


@login_required
def multiple_images(request, slug_fireball):
    # Maneja un formulario con la opcion de subir varias imágenes a la ves
    template = "hisoka/multiple_images.html"
    fireball = Fireball.objects.get(slug=slug_fireball)

    if request.method == "POST":
        files = request.FILES.getlist('images')
        for x in files:
            FeralSpirit.objects.create(tipo="imagen", imagen=x, fireball=fireball)
        return redirect('fireball', slug_fireball=fireball.slug, queryset='ultima_publicacion')

    context = {'fireball': fireball}
    return render(request, template, context)


@login_required
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


@login_required
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


@login_required
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
            return HttpResponse("No hay feral_id", status=400)
    else:
        return HttpResponse("No es Ajax", status=400)


# Magic
class MagicPy(TemplateView):

    template_name = "hisoka/magic_py.html"

    def get_context_data(self, **kwargs):
        context = super(MagicPy, self).get_context_data()
        grupos_magicpy = GrupoMagicPy.objects.filter(eliminado=False).annotate(num_cartas=Count('cartamagicpy'))
        for grupo in grupos_magicpy:
            print grupo.nombre
            print grupo.num_cartas

        context['grupos_magicpy'] = grupos_magicpy
        return context


class CartaMPy(TemplateView):

    template_name = "hisoka/carta_mpy.html"

    def get_context_data(self, **kwargs):
        context = super(CartaMPy, self).get_context_data()
        carta_id = self.kwargs['id_carta']
        carta_magicpy = CartaMagicPy.objects.get(id=carta_id)
        context['carta_magicpy'] = carta_magicpy
        carta_magicpy.save()

        # Actualiza Ultima Revisión
        carta_magicpy.ultima_revision = datetime.today()

        relaciones_obj = CartaConjunto.objects.filter(carta=carta_magicpy, eliminado=False).select_related('conjunto')
        if relaciones_obj:
            conjuntos_carta = [x.conjunto for x in relaciones_obj]
            context['conjuntos'] = conjuntos_carta
        else:
            context['conjuntos'] = None
        return context


@login_required
def info_carta(request):
    # API punto de entrada. Envía un JSON con la información de la carta
    if request.is_ajax():
        id_carta = request.GET.get("id_carta")
        nombre_carta = request.GET.get("nombre_carta")

        if not id_carta and not nombre_carta:
            return HttpResponse(status=400)
        else:
            if id_carta:
                id_carta = id_carta.strip()
                carta = CartaMagicPy.objects.get(id=id_carta)
            else:
                carta = CartaMagicPy.objects.get(nombre=nombre_carta)

            carta = {'nombre': carta.nombre, 'nombre_carta_magin': carta.nombre_carta_magic,
                     'grupo': carta.grupo.nombre, 'descripcion': carta.descripcion, 'id_carta': carta.id,
                     'imagen': carta.imagen.url, 'url_carta': reverse('carta_magicpy', kwargs={'id_carta': carta.id})}

        return HttpResponse(json.dumps(carta))


class GrupoMPy(TemplateView):

    template_name = "hisoka/grupo_mpy.html"

    def get_context_data(self, **kwargs):
        context = super(GrupoMPy, self).get_context_data()
        grupo_id = self.kwargs['id_grupo']
        grupo_magicpy = GrupoMagicPy.objects.get(id=grupo_id)
        context['grupo_magicpy'] = grupo_magicpy

        grupo_magicpy.ultima_revision = datetime.today()
        grupo_magicpy.save()

        cartas_magicpy = CartaMagicPy.objects.filter(grupo=grupo_magicpy, eliminada=False)
        context['cartas_magicpy'] = cartas_magicpy
        return context


@login_required
def nueva_carta(request):
    template = "hisoka/nueva_carta.html"

    if request.method == "POST":

        form = FormNuevaCarta(request.POST)

        if form.is_valid():

            carta = form.save(commit=False)

            imagen_url = form.cleaned_data['imagen_url']
            respuesta = requests.get(imagen_url)
            imagen = Image.open(StringIO(respuesta.content))
            stringio_obj = StringIO()
            imagen.save(stringio_obj, format="JPEG")
            final_image = stringio_obj.getvalue()

            carta.ultima_revision = datetime.today()
            carta.save()

            archivo_imagen = ContentFile(final_image, "0_" + carta.nombre)  # Guarda la original con un 0 adelante
            carta.imagen_base.save("0_" + carta.nombre, archivo_imagen, save=True)

            return redirect('recortar_carta', id_carta=carta.id)

    else:
        form = FormNuevaCarta()

    context = {'form': form}
    return render(request, template, context)


@login_required
def relacionar_carta(request):
    template = "hisoka/relacionar_carta.html"

    if request.method == "POST":
        pass

    else:
        pass

    cartas_obj = CartaMagicPy.objects.filter(eliminada=False)
    cartas_autocomplete = []
    for c in cartas_obj:
        cartas_autocomplete.append({'label': str(c.id) + " . " + c.nombre + " - " + c.grupo.nombre, 'value': c.nombre})

    context = {'cartas_autocomplete': json.dumps(cartas_autocomplete)}

    return render(request, template, context)


class NuevoGrupo(CreateView):
    template_name = "hisoka/nuevo_grupo.html"

    form_class = FormNuevoGrupo
    success_url = reverse_lazy('hisokas_main')  # Cambiar

    def form_valid(self, form):
        form.instance.ultima_revision = datetime.today()
        return super(NuevoGrupo, self).form_valid(form)


class RecortarCarta(TemplateView):
    template_name = "hisoka/recortar_carta.html"

    def get_context_data(self, **kwargs):
        context = super(RecortarCarta, self).get_context_data()
        carta_magicpy = CartaMagicPy.objects.get(id=self.kwargs['id_carta'])
        context['carta_magicpy'] = carta_magicpy
        return context


@login_required
def recortar_carta_ajax(request):

    if request.is_ajax():

        print request.POST
        carta_id = request.POST.get("carta_id")
        puntos_recortar = request.POST.get("imagen")

        print puntos_recortar

        # carta_magicpy = CartaMagicPy.objects.get(id=carta_id)
        # nombre_archivo = carta_magicpy.nombre + ".jpeg"
        # imagen_django = ContentFile(imagen_decodificada, nombre_archivo)
        # carta_magicpy.imagen.save(nombre_archivo, imagen_django, save=True)
        # url_redirect = reverse('carta_magicpy', kwargs={'id_carta': carta_magicpy.id})

        #print url_redirect
        #return HttpResponse(url_redirect)
        return HttpResponse("veamos")

    else:
        return HttpResponse(status=400)


class ConjuntoMPy(TemplateView):
    template_name = "hisoka/conjunto_magicpy.html"

    def get_context_data(self, **kwargs):
        context = super(ConjuntoMPy, self).get_context_data()
        conjunto_magicpy = ConjuntoCartas.objects.get(id=self.kwargs['id_conjunto'])
        context['conjunto_magicpy'] = conjunto_magicpy
        cartas_conjunto_obj = conjunto_magicpy.cartaconjunto_set.all()
        cartas_conjunto = []
        for c in cartas_conjunto_obj:
            print c.carta
            cartas_conjunto.append(c.carta)
        print cartas_conjunto
        context['cartas_conjunto'] = cartas_conjunto
        return context


@login_required
def guardar_conjunto(request):

    """ Procesa con ajax las ids de las cartas relacionadas y crea un objeto conjunto """

    if request.is_ajax():

        descripcion = request.POST.get("descripcion")
        id_cartas = json.loads(request.POST.get('id_cartas'))
        nombre = request.POST.get("nombre")

        # Crear objeto Conjunto Cartas
        conjunto_magicpy = ConjuntoCartas.objects.create(nombre=bleach.clean(nombre), descripcion=bleach.clean(descripcion),
                                      fecha_creacion=datetime.today(), ultima_revision=datetime.today())
        for carta_id in id_cartas:
            carta = CartaMagicPy.objects.get(id=int(carta_id))
            CartaConjunto.objects.create(carta=carta, conjunto=conjunto_magicpy)

        url_conjunto = reverse('conjunto_magicpy', kwargs={'id_conjunto': conjunto_magicpy.id})
        return HttpResponse(url_conjunto)

    else:
        return HttpResponse(status=400)
