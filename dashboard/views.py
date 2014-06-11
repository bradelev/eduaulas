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

	print('funcio ini')
	var_areas = Area.objects.all()
	var_subjects = Subject.objects.all()
	var_units = Unit.objects.all()
	"""if request.POST:
        
        id_area =request.POST['id_area']
	var_subjects = Subject.objects.all()
	var_units = Unit.objects.all()"""

	return render_to_response('panel2.html',{'areas':var_areas,'subjects':var_subjects, 'units':var_units }, context_instance = RequestContext(request))

	


def list_students(request):
	#print('fuera del post')
	#if request.POST:

	#	var_unit =request.POST['unit'] 
	#	print('dentro del post')
	#	print(var_unit, Unidad)
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
