from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	url(r'^', include('teacher.urls')),

	url(r'^alumnos/', include('student.urls')),
	url(r'^aulas/', include('classroom.urls')),
	#url(r'^docente/', include('teacher.urls')),
	url(r'^panel/', include('dashboard.urls')),
	url(r'^contenidos/', include('exercise.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cargarDatos/', 'datosTest.cargarDatosTest.ingresar_datos'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 	
