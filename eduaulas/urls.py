from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^aulas/', include('classroom.urls')),
	#url(r'^docente/', include('teacher.urls')),
	url(r'^panel/', include('dashboard.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
