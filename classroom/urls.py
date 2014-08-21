from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'^$', 'classroom.views.ini_redirect'),
	url(r'lista/$', 'classroom.views.ini'),
	url(r'departments/$', 'classroom.views.load_departments'),
	url(r'schools/$', 'classroom.views.load_schools'),
	url(r'agregar/aula/$', 'classroom.views.classroom_save_add'),
	
	url(r'eliminar/aula/$', 'classroom.views.classroom_delete'),
	url(r'editar/aula/$', 'classroom.views.classroom_save_edit'),
	url(r'cargar/aula/$', 'classroom.views.load_classroom'),
	url(r'cargar/codigo_aula/$', 'classroom.views.load_classroom_code'),
	url(r'aulas/$', 'classroom.views.classroom_list'),
	url(r'cargar_form/$', 'classroom.views.load_classroom_form'),
	url(r'datos_docente/$', 'classroom.views.load_teacher'),
	url(r'actualizar_datos/$', 'classroom.views.update_teacher_info'),
	url(r'actualizar_configuracion/$', 'classroom.views.update_teacher_configuration'),
	url(r'configuracion_docente/$', 'classroom.views.load_teacher_configuration'),


)