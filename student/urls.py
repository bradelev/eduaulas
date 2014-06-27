from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'lista/(?P<code>\w+)?/?$', 'student.views.students_list'),
	url(r'info_alumno/(?P<id>\w+)?/?$', 'student.views.student_info'),
   
	
)