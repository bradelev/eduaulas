from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'^$','exercise.views.contents'),
	url(r'^(?P<code>\w+)?/(?P<subject>\w+)?/(?P<unit>\w+)?/ejercicio/(?P<number>\d+)?/$', 'exercise.views.specific_content'),
	#url(r'^(?P<excercise>\d+)?/?/$', 'exercise.views.img'),
)