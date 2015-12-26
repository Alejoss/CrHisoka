from django.conf.urls import include, url
from django.contrib import admin

from inicio import views
# from hisoka import urls as hisoka_urls

urlpatterns = [
    url(r'^$', views.Inicio.as_view(), name="inicio"),
    url(r'^cripto_blog/$', views.CriptoBlog.as_view(), name="cripto_blog"),
    url(r'^cripto_videos/$', views.CriptoVideos.as_view(), name="cripto_videos"),
    
    url(r'^historia_conciencia_poder/$', views.HistoriaConcienciaPoder.as_view(), name="historia_conciencia_poder"),
    
    url(r'^criptoanarquismo_unica_salida/$', views.CriptoUnicaSalida.as_view(), name="criptoanarquismo_unica_salida"),    
    url(r'^jardin_bonsais/$', views.JardinBonsais.as_view(), name="jardin_bonsais"),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Hisoka
    url(r'^hisoka/', include('hisoka.urls')),
]
