from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	
	url(r'^(?P<grade>\d+)?/(?P<subject>\w+)?/(?P<unit>\w+)?/$', 'exercise.views.contents'),
)