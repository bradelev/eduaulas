from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^aulas/', include('aulas.urls')),
	url(r'^docente/', include('docente.urls')),
	url(r'^panel/', include('panel.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
