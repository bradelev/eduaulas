from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'lista/$', 'classroom.views.lista'),

	url(r'crear/$', 'classroom.views.crear'),
	#url(r'borrar/$', 'aulas.views.lista'),
	url(r'compartir/$', 'classroom.views.compartir'),
	url(r'detalle/(?P<id>\d+)?/', 'classroom.views.detalle')
)