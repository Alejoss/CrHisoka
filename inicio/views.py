# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from hisoka.models import FeralSpirit


class Inicio(TemplateView):
    template_name = "inicio/inicio.html"


class HistoriaConcienciaPoder(TemplateView):
    template_name = "inicio/historia_poder_conciencia.html"

    def get_context_data(self, **kwargs):
        context = {'seccion': 'historia_conciencia_poder'}
        return context


class CriptoBlog(TemplateView):
    template_name = "inicio/criptoblog.html"

    def get_context_data(self, **kwargs):
        context = {'seccion': 'cripto_blog'}
        return context


class CriptoVideos(TemplateView):
    template_name = "inicio/criptovideos.html"

    def get_context_data(self, **kwargs):
        context = {'seccion': 'cripto_videos'}
        return context


class ContenidoExtra(ListView):
    template_name = "inicio/contenido_extra.html"
    context_object_name = "feral_spirits"

    def get_queryset(self):
        ferals = FeralSpirit.objects.filter(fireball__nombre="Criptolibertad", eliminado=False)
        print ferals
        return ferals

    def get_context_data(self, **kwargs):
        context = super(ContenidoExtra, self).get_context_data(**kwargs)
        context['seccion'] = 'contenido_extra'
        print context
        return context


# Blog
class CriptoUnicaSalida(TemplateView):
    template_name = "inicio/el_cr_unica_salida.html"

    def get_context_data(self, **kwargs):
        context = super(CriptoUnicaSalida, self).get_context_data(**kwargs)
        context['active'] = 'cripto_unica_salida'
        context['seccion'] = 'cripto_blog'
        return context

class JardinBonsais(TemplateView):
    template_name = "inicio/jardin_bonsais.html"

    def get_context_data(self, **kwargs):
        context = super(JardinBonsais, self).get_context_data(**kwargs)
        context['active'] = 'jardin_bonsais'
        context['seccion'] = 'cripto_blog'
        return context

class QueEsCripto(TemplateView):
    template_name = "inicio/que_es_cripto.html"

    def get_context_data(self, **kwargs):
        context = super(QueEsCripto, self).get_context_data(**kwargs)
        context['active'] = 'que_es_cripto'
        context['seccion'] = 'cripto_blog'
        return context


# Videos
class VPrologo(TemplateView):
    template_name = "inicio/v_prologo.html"

    def get_context_data(self, **kwargs):
        context = super(VPrologo, self).get_context_data(**kwargs)
        context['active'] = 'v_prologo'
        context['seccion'] = 'cripto_videos'
        return context


class VConciencia(TemplateView):
    template_name = "inicio/v_conciencia.html"

    def get_context_data(self, **kwargs):
        context = super(VConciencia, self).get_context_data(**kwargs)
        context['active'] = 'v_conciencia'
        context['seccion'] = 'cripto_videos'
        return context


class VPoder(TemplateView):
    template_name = "inicio/v_poder.html"

    def get_context_data(self, **kwargs):
        context = super(VPoder, self).get_context_data(**kwargs)
        context['active'] = 'v_poder'
        context['seccion'] = 'cripto_videos'
        return context


class VCastillo(TemplateView):
    template_name = "inicio/v_castillo.html"

    def get_context_data(self, **kwargs):
        context = super(VCastillo, self).get_context_data(**kwargs)
        context['active'] = 'v_castillo'
        context['seccion'] = 'cripto_videos'
        return context


class VCaverna(TemplateView):
    template_name = "inicio/v_caverna.html"

    def get_context_data(self, **kwargs):
        context = super(VCaverna, self).get_context_data(**kwargs)
        context['active'] = 'v_caverna'
        context['seccion'] = 'cripto_videos'
        return context


class VMitologia(TemplateView):
    template_name = "inicio/v_mitologia.html"

    def get_context_data(self, **kwargs):
        context = super(VMitologia, self).get_context_data(**kwargs)
        context['active'] = 'v_mitologia'
        context['seccion'] = 'cripto_videos'
        return context


class VDemocracia(TemplateView):
    template_name = "inicio/v_democracia.html"

    def get_context_data(self, **kwargs):
        context = super(VDemocracia, self).get_context_data(**kwargs)
        context['active'] = 'v_democracia'
        context['seccion'] = 'cripto_videos'
        return context


class VTemplo(TemplateView):
    template_name = "inicio/v_templo.html"

    def get_context_data(self, **kwargs):
        context = super(VTemplo, self).get_context_data(**kwargs)
        context['active'] = 'v_templo'
        context['seccion'] = 'cripto_videos'
        return context
