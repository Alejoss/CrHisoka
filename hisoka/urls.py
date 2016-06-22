from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib import admin

from hisoka import views

urlpatterns = [

    url(r'^login/$', auth_views.login, {'template_name': 'hisoka/hisoka_login.html'}, name="login"),

    url(r'^hisokas_main/$', views.HisokasMain.as_view(), name="hisokas_main"),

    url(r'^fireball/(?P<slug_fireball>[-\w]+)/(?P<queryset>\w+)/$',
        views.FireballDetail.as_view(), name="fireball"),

    url(r'^magic_py/$', views.MagicPy.as_view(), name="magic_py"),

    # Forms>
    url(r'^crear_fireball/$', views.CrearFireball.as_view(),
        name="crear_fireball"),

    url(r'^crear_feral/(?P<slug_fireball>[-\w]+)/(?P<tipo_feral>\w+)/$',
        views.CrearFeralSpirit.as_view(),
        name="crear_feral_spirit"),

    url(r'^editar_feral/$', views.editar_feral,
        name="editar_feral_spirit"),

    url(r'^eliminar_feral/$', views.eliminar_feral,
        name="eliminar_feral_spirit"),

    url(r'^nueva_carta/$', views.NuevaCarta.as_view(),
        name="nueva_carta"),

    url(r'^nuevo_grupo/$', views.NuevoGrupo.as_view(),
        name="nuevo_grupo"),

    # API
    url(r'^feral_data/$', views.feral_data,
        name="feral_data"),
]
