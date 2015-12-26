from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib import admin

from hisoka import views

urlpatterns = [

    url(r'^login/$', auth_views.login, {'template_name': 'hisoka/hisoka_login.html'}, name="login"),

    url(r'^hisokas_main/$', views.HisokasMain.as_view(), name="hisokas_main"),

    url(r'^fireball/(?P<slug_fireball>[-\w]+)/(?P<queryset>\w+)/$', 
    	views.FireballDetail.as_view(), name="fireball"),

    # Forms
	url(r'^crear_fireball/$', views.CrearFireball.as_view(), 
		name="crear_fireball"),

	url(r'^crear_feral/(?P<slug_fireball>[-\w]+)/$',
		views.CrearFeralSpirit.as_view(),
		name="crear_feral_spirit")
]
