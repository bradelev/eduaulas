from django.conf.urls import patterns, include, url
from exercise.api.resources import ResultResource, TeacherCommentsResource
from student.api.resources import StudentResource
from tastypie.api import Api
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

api = Api(api_name="v1")
api.register(ResultResource())
api.register(TeacherCommentsResource())
api.register(StudentResource())

urlpatterns = patterns('',
	url(r'^api/', include(api.urls)),
	url(r'^$', include('classroom.urls')),
	url(r'^', include('teacher.urls')),
	url(r'^alumnos/', include('student.urls')),
	url(r'^aulas/', include('classroom.urls')),
	url(r'^panel/', include('dashboard.urls')),
	url(r'^contenidos/', include('exercise.urls')),
	url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 	
