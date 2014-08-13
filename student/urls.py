from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'listas/(?P<code>\w+)?/?$', 'student.views.ini'),
	url(r'listas/(?P<code>\w+)?/obtener?$', 'student.views.students_info'),
	url(r'info_alumno/(?P<code>\w+)/(?P<id>\w+)/?$', 'student.views.student_info'),
	#url(r'estadisticas_por_areas/(?P<code>\w+)/?$', 'student.views.ini_stats_by_topics'),
	#url(r'estadisticas_por_areas/(?P<code>\w+)/obtener/?$', 'student.views.stats_by_topics'),
	url(r'estadisticas_por_areas/(?P<code>\w+)/?$', 'student.views.stats_by_topics'),

	url(r'estadisticas_por_perfiles/(?P<code>\w+)/?$', 'student.views.stats_by_learning_profiles'),
   
	
)