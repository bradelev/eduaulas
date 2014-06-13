from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'lista/$', 'classroom.views.ini'),
	url(r'departments/$', 'classroom.views.load_departments'),
	url(r'agregar/aula/$', 'classroom.views.classroom_save'),
	url(r'aulas/$', 'classroom.views.classroom_list'),
	url(r'cargar_form/$', 'classroom.views.load_classroom_form'),
	#url(r'borrar/$', 'aulas.views.lista'),
	#url(r'compartir/$', 'classroom.views.compartir'),
	#url(r'detalle/(?P<id>\d+)?/', 'classroom.views.detalle')
)