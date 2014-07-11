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

	

def ini(request,code):
	var_areas = Area.objects.all()
	#var_subjects = Subject.objects.all()
	#var_units = Unit.objects.all()
	return render_to_response('panel.html',{'areas':var_areas,'code':code}, context_instance = RequestContext(request))	

def load_filters_subject(request,code):
	message = ""
	type = "error"
	dictionary_subjects = {}
	try:

		if request.POST:
			id_area =request.POST['id_area']										
			a = Area.objects.get(pk=id_area)
			var_subjects = Subject.objects.filter(area=a)
					
			for y in var_subjects:				
				dictionary_subjects[y.id] = {
					
					"name": y.name,
					"id": y.id					
				}
	except ClassRoom.DoesNotExist:
	        message = "No hay aulas"
	result = simplejson.dumps({
	                "dictionary_subjects":dictionary_subjects,
	                "code":code,
	                "message":message,
	                "type":type,
	        }, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')
	



def load_filters_unit(request,code):
	print('cargo UNIDADES')
	dictionary_units = {}
	message = ""
	type = "error"
	
	try:
		if request.POST:
			
			id_subject =request.POST['id_subject']			
			s = Subject.objects.get(pk=id_subject)
			var_units = Unit.objects.filter(subject=s)
			
			
			for p in var_units:				
				dictionary_units[p.id] = {
					
					"name": p.name,
					"id": p.id								
					
				}
		
			type = "success"	
			result = simplejson.dumps({
			"dictionary_units":dictionary_units,
			"message":message,
			"type":type,
			}, cls = LazyEncoder)
			return HttpResponse(result, mimetype = 'application/javascript')

	except Unit.DoesNotExist:
		message = "No hay unidades"
	return HttpResponse(result, mimetype = 'application/javascript')



def list_students(request,code):

	dictionary_students = {}
	dictionary_students_exercises = {}
	dictionary_units_exercises={}
	message = ""
	type = "error"
	try:
		if request.POST:

			id_unit =request.POST['id_unit']
			var_unit = Unit.objects.get(pk=id_unit)			
			cl = ClassRoom.objects.get(pk=code)
			students = Student.objects.filter(class_room=cl)
			var_units_exercises = Exercise.objects.filter(unit=var_unit)
			#var_students_exercises = Result.objects.filter(student=students, exercise=var_units_exercises)
			
			type = "success"
			
			for c in students:
				for j in var_units_exercises:
					var_results = Result.objects.filter(exercise=j, student=c)	
					
					if var_results.exists():
						print('tiene ejerciio', c.id, j.id)
						for r in var_results:
							dictionary_students_exercises[j.id] = {
								"points": r.points,
								"student": r.student.id				
								
							}
					else:
						print('no tiene ejerciio',c.id, j.id)
						dictionary_students_exercises[j.id] = {
								"points": '',
								"student":c.id			
								
							}
				

			"""for y in var_students_exercises:				
				dictionary_students_exercises[y.id] = {
					
					"points": y.points,
					"student": y.student.id				
					
				}"""
			
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

	

	