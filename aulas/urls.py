from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'lista/$', 'aulas.views.lista'),

	url(r'crear/$', 'aulas.views.crear'),
	#url(r'borrar/$', 'aulas.views.lista'),
	url(r'compartir/$', 'aulas.views.compartir'),
	url(r'detalle/(?P<id>\d+)?/', 'aulas.views.detalle')
)