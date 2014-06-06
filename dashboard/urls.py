from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'lista/$', 'dashboard.views.lista'),

	url(r'crear/$', 'dashboard.views.crear'),
	#url(r'borrar/$', 'aulas.views.lista'),
	url(r'compartir/$', 'dashboard.views.compartir'),
)