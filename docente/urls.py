from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'registro/$', 'aulas.views.registro'),
	url(r'ingresar/$', 'aulas.views.ingresar'),
	url(r'password/$', 'aulas.views.password'),
)