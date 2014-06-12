from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	url(r'^', include('teacher.urls')),


	url(r'^aulas/', include('classroom.urls')),
	#url(r'^docente/', include('teacher.urls')),
	url(r'^panel/', include('dashboard.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cargarDatos/', 'datosTest.cargarDatosTest.ingresar_datos')
)
