from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'^(?P<code>\w+)?/?$', 'exercise.views.ini'),
	url(r'^(?P<code>\w+)?/materias/$', 'exercise.views.load_filters_subject'),
	url(r'^(?P<code>\w+)?/unidades/$', 'exercise.views.load_filters_unit'),
	url(r'ejercicio/(?P<code>\w+)/(?P<id>\d+)?/$', 'exercise.views.specific_content_id'),
	url(r'^(?P<code>\w+)?/contenidos/$', 'exercise.views.list_contents'),
	url(r'^(?P<grade>\w+)?/(?P<subject>\w+)?/(?P<unit>\w+)?/ejercicio/(?P<number>\d+)?/$', 'exercise.views.specific_content'),
	
	#url(r'^(?P<excercise>\d+)?/?/$', 'exercise.views.img'),
)
