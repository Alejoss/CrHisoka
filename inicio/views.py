# from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class Inicio(TemplateView):
	template_name = "inicio/inicio.html"


class HistoriaConcienciaPoder(TemplateView):
	template_name = "inicio/historia_poder_conciencia.html"


class CriptoBlog(TemplateView):
	template_name = "inicio/criptoblog.html"


class CriptoVideos(TemplateView):
	template_name = "inicio/criptovideos.html"


class CriptoUnicaSalida(TemplateView):
	template_name = "inicio/el_cr_unica_salida.html"


class JardinBonsais(TemplateView):
	template_name = "inicio/jardin_bonsais.html"
