from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'list/$', 'classroom.views.classroom_list'),

	url(r'add/$', 'classroom.views.classroom_add'),
	#url(r'borrar/$', 'aulas.views.lista'),
	url(r'compartir/$', 'classroom.views.compartir'),
	url(r'detalle/(?P<id>\d+)?/', 'classroom.views.detalle')
)