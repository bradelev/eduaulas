from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^$', 'teacher.views.inicio'),
    url(r'^login/','teacher.views.login_user'),
    url(r'^inicio/', 'teacher.views.inicio'),
    url(r'^registro/', 'teacher.views.register'),
    url(r'^logout/', 'teacher.views.logout_view'),
    url(r'^registro_exitoso/', 'teacher.views.register_success'),
	
)