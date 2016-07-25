# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from hisoka.models import FeralSpirit


class Inicio(TemplateView):
    template_name = "inicio/inicio.html"


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


class PoderInformacion(TemplateView):
    template_name = "inicio/poder_informacion.html"

    def get_context_data(self, **kwargs):
        context = super(PoderInformacion, self).get_context_data(**kwargs)
        context['active'] = 'poder_informacion'
        context['seccion'] = 'cripto_blog'
        return context


# Videos
class HistoriaConcienciaPoder(TemplateView):
    template_name = "inicio/historia_poder_conciencia.html"

    def get_context_data(self, **kwargs):
        context = super(HistoriaConcienciaPoder, self).get_context_data(**kwargs)
        context['seccion'] = 'historia_conciencia_poder'
        return context


class MitoApocalipsis(TemplateView):
    template_name = "inicio/mito_apocalipsis.html"

    def get_context_data(self, **kwargs):
        context = super(MitoApocalipsis, self).get_context_data(**kwargs)
        context['active'] = 'mito_apocalipsis'
        context['seccion'] = 'cripto_videos'
        return context


class BlockBitLibertad(TemplateView):
    template_name = "inicio/block_bit_libertad.html"

    def get_context_data(self, **kwargs):
        context = super(BlockBitLibertad, self).get_context_data(**kwargs)
        context['active'] = 'block_bit_libertad'
        context['seccion'] = 'cripto_videos'
        return context


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


class VTeismo(TemplateView):
    template_name = "inicio/v_teismo.html"

    def get_context_data(self, **kwargs):
        context = super(VTeismo, self).get_context_data(**kwargs)
        context['active'] = 'v_teismo'
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


class VMonopolios(TemplateView):
    template_name = "inicio/v_monopolios.html"

    def get_context_data(self, **kwargs):
        context = super(VMonopolios, self).get_context_data(**kwargs)
        context['active'] = 'v_monopolios'
        context['seccion'] = 'cripto_videos'
        return context


class VBomberos(TemplateView):
    template_name = "inicio/v_bomberos.html"

    def get_context_data(self, **kwargs):
        context = super(VBomberos, self).get_context_data(**kwargs)
        context['active'] = 'v_bomberos'
        context['seccion'] = 'cripto_videos'
        return context


class VEnergia(TemplateView):
    template_name = "inicio/v_energia.html"

    def get_context_data(self, **kwargs):
        context = super(VEnergia, self).get_context_data(**kwargs)
        context['active'] = 'v_energia'
        context['seccion'] = 'cripto_videos'
        return context


class VCarreteras(TemplateView):
    template_name = "inicio/v_carreteras.html"

    def get_context_data(self, **kwargs):
        context = super(VCarreteras, self).get_context_data(**kwargs)
        context['active'] = 'v_carreteras'
        context['seccion'] = 'cripto_videos'
        return context


class VMedicina(TemplateView):
    template_name = "inicio/v_medicina.html"

    def get_context_data(self, **kwargs):
        context = super(VMedicina, self).get_context_data(**kwargs)
        context['active'] = 'v_medicina'
        context['seccion'] = 'cripto_videos'
        return context
