from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'lista/$', 'dashboard.views.lista'),
	url(r'lista/(?P<unit_id>\d+)?/?$', 'dashboard.views.lista2'),
	url(r'crear/$', 'dashboard.views.crear'),
	#url(r'borrar/$', 'aulas.views.lista'),
	url(r'compartir/$', 'dashboard.views.compartir'),
)