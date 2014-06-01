from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'registro/$', 'teacher.views.registro'),
	url(r'ingresar/$', 'teacher.views.ingresar'),
	url(r'password/$', 'teacher.views.password'),
)