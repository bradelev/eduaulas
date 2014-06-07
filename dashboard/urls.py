from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	
	url(r'$', 'dashboard.views.ini'),
	url(r'list/$', 'dashboard.views.list_students'),
	#url(r'borrar/$', 'aulas.views.lista'),

)