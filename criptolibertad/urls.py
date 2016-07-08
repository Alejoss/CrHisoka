from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from inicio import views
# from hisoka import urls as hisoka_urls

urlpatterns = [
    url(r'^$', views.Inicio.as_view(), name="inicio"),
    url(r'^cripto_blog/$', views.CriptoBlog.as_view(), name="cripto_blog"),
    url(r'^cripto_videos/$', views.CriptoVideos.as_view(), name="cripto_videos"),
    
    url(r'^historia_conciencia_poder/$', views.HistoriaConcienciaPoder.as_view(), name="historia_conciencia_poder"),

    # Blog
    url(r'^criptoanarquismo_unica_salida/$', views.CriptoUnicaSalida.as_view(), name="cripto_unica_salida"),
    url(r'^jardin_bonsais/$', views.JardinBonsais.as_view(), name="jardin_bonsais"),
    url(r'^que_es_criptoanarquismo/$', views.QueEsCripto.as_view(), name="que_es_cripto"),
    url(r'^contenido_extra/$', views.ContenidoExtra.as_view(), name="contenido_extra"),

    # Videos
    url(r'^v_prologo/$', views.VPrologo.as_view(), name="v_prologo"),
    url(r'^v_conciencia/$', views.VConciencia.as_view(), name="v_conciencia"),
    url(r'^v_poder/$', views.VPoder.as_view(), name="v_poder"),
    url(r'^v_teismo/$', views.VTeismo.as_view(), name="v_teismo"),
    url(r'^v_castillo/$', views.VCastillo.as_view(), name="v_castillo"),
    url(r'^v_caverna/$', views.VCaverna.as_view(), name="v_caverna"),
    url(r'^v_mitologia/$', views.VMitologia.as_view(), name="v_mitologia"),
    url(r'^v_democracia/$', views.VDemocracia.as_view(), name="v_democracia"),
    url(r'^v_templo/$', views.VTemplo.as_view(), name="v_templo"),
    url(r'^v_monopolios/$', views.VMonopolios.as_view(), name="v_monopolios"),
    url(r'^v_bomberos/$', views.VBomberos.as_view(), name="v_bomberos"),
    url(r'^v_energia/$', views.VEnergia.as_view(), name="v_energia"),
    url(r'^v_carreteras/$', views.VCarreteras.as_view(), name="v_carreteras"),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Hisoka
    url(r'^login/$', auth_views.login, {'template_name': 'hisoka/hisoka_login.html'}, name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': reverse_lazy('inicio')}, name="logout"),
    url(r'^hisoka/', include('hisoka.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
