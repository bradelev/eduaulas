from django.shortcuts import render_to_response
from django.template import RequestContext
from student.models import Student
from classroom.models import  ClassRoom
from exercise.models import Unit, Exercise, Result, Area, Subject
from django.utils import simplejson
from django.http import *
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

class LazyEncoder(simplejson.JSONEncoder):
	"""Encodes django's lazy i18n strings."""
    
   
	def default(self, obj):
	    if isinstance(obj, Promise):
	    	return force_unicode(obj)
	    return obj  

	

def ini(request):
	var_areas = Area.objects.all()
	#var_subjects = Subject.objects.all()
	#var_units = Unit.objects.all()

	if request.POST:
		
		id_area =request.POST['id_area']
		dictionary_subjects = {}
		message = ""
		type = "error"
		try:										
			a = Area.objects.get(pk=id_area)
			var_subjects = Subject.objects.filter(area=a)
			
			type = "success"
			
			for y in var_subjects:				
				dictionary_subjects[y.id] = {
					
					"name": y.name,
					"id": y.id
								
					
				}
			
		except Subject.DoesNotExist:
			message = "No hay materias"
		result = simplejson.dumps({
				"dictionary_subjects":dictionary_subjects,
				"message":message,
				"type":type,
			}, cls = LazyEncoder)
		return HttpResponse(result, mimetype = 'application/javascript')
		
		
	return render_to_response('panel2.html',{'areas':var_areas}, context_instance = RequestContext(request))

def load_filters_unit(request):
	
	dictionary_units = {}
	message = ""
	type = "error"
	
	try:
		if request.POST:
			
			id_subject =request.POST['id_subject']
			print('materia', id_subject)
			s = Subject.objects.get(pk=id_subject)
			var_units = Unit.objects.filter(subject=s)
			#var_units = Subject.objects.all()
			type = "success"
			
			for p in var_units:				
				dictionary_units[p.id] = {
					
					"name": p.name,
					"id": p.id
								
					
				}
		
	except Unit.DoesNotExist:
		message = "No hay unidades"
	result = simplejson.dumps({
			"dictionary_units":dictionary_units,
			"message":message,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')


def list_students(request):

	dictionary_students = {}
	dictionary_students_exercises = {}
	dictionary_units_exercises={}
	message = ""
	type = "error"
	try:
		var_unit = Unit.objects.get(pk=1)
		#cl = ClassRoom.objects.get(pk='efr5g')
		students = Student.objects.filter()
		var_units_exercises = Exercise.objects.filter(unit=var_unit)
		var_students_exercises = Result.objects.filter(student=students, exercise=var_units_exercises)

		type = "success"
		for y in var_students_exercises:				
			dictionary_students_exercises[y.id] = {
				
				"points": y.points,
				"student": y.student.id				
				
			}
		
		for x in students:
			dictionary_students[x.id] = {
			"id_student":x.id,
			"name": x.name,
			"last_name": x.last_name
			}
		for e in var_units_exercises:				
			dictionary_units_exercises[e.id] = {				
				"exercise_id": e.exercise_id			
				
			}	

	
	except Student.DoesNotExist:
		message = "No hay alumnos"
	result = simplejson.dumps({
			"dictionary_students":dictionary_students,
			"dictionary_students_exercises":dictionary_students_exercises,
			"dictionary_units_exercises":dictionary_units_exercises,
			"message":message,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')

	#return render_to_response('panel2.html',{'students':students,'ex':exercises, 'results': var_results }, context_instance = RequestContext(request))


	"""def list_students(request):
	print("entra")
	#print("no entra")
	#if request.is_ajax():
	#print("entra")
	dictionary_students = {}
	message = ""
	type = "error"
	try:
		var_unit = Unit.objects.get(pk=1)
		#cl = ClassRoom.objects.get(pk='efr5g')
		students = Student.objects.filter()
		exercises = Exercise.objects.filter(unit=var_unit)
		var_results = Result.objects.filter(student=students, exercise=exercises)

		type = "success"
		for x in students:				
			dictionary_students[x.id] = {
				
				"name": x.name,
				"last_name": x.last_name
				
			}
		
	except Student.DoesNotExist:
		message = "No hay alumnos"
	result = simplejson.dumps({
			"dictionary_students":dictionary_students,
			"message":message,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')"""
