from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	
	url(r'list/$', 'dashboard.views.ini'),
	url(r'list/units/$', 'dashboard.views.load_filters_unit'),
	url(r'students/$', 'dashboard.views.list_students'),
	

)