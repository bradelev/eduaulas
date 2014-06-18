from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	
	#url(r'lista/(?P<code>\w+)?/?$', 'dashboard.views.ini'),
	url(r'lista/$', 'dashboard.views.ini'),
	url(r'lista/unidades/$', 'dashboard.views.load_filters_unit'),
	#url(r'lista/(?P<code>\w+)?/unidades/$', 'dashboard.views.load_filters_unit'),
	url(r'alumnos/$', 'dashboard.views.list_students'),
	
	

)