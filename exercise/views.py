from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from classroom.models import  ClassRoom, Grade
from exercise.models import Exercise, Lecture, Subject, Unit
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
	return render_to_response('contents.html',{'areas':var_areas}, context_instance = RequestContext(request))	

def load_filters_subject(request, code):
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
	                "message":message,
	                "type":type,
	        }, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')
	



def load_filters_unit(request,code):
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
			matriz = []
			type = "success"
			i=0
				
			for s in students:
				matriz.append([])
				matriz[i].append(s.name)
				matriz[i].append(s.last_name)
				#j = j + 1
				print(s.name)
				for j in var_units_exercises:
					var_results = Result.objects.filter(exercise=j, person=s)						
					if var_results.exists():
						for r in var_results:
							matriz[i].append(r.points)
						
					else:
						matriz[i].append('9')
				i = i + 1	
			print(matriz)

			for e in var_units_exercises:				
				dictionary_units_exercises[e.id] = {				
					"exercise_id": e.cuasimodo_exercise_id			
					
				}	

	
	except Student.DoesNotExist:
		message = "No hay alumnos"
	result = simplejson.dumps({
			"dictionary_units_exercises":dictionary_units_exercises,
			"matriz":matriz,
			"message":message,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')

	




# Create your views here.

class LazyEncoder(simplejson.JSONEncoder):
	"""Encodes django's lazy i18n strings."""
    
   
	def default(self, obj):
	    if isinstance(obj, Promise):
	    	return force_unicode(obj)
	    return obj  

def contents(request):

	return render_to_response('contents.html', context_instance=RequestContext(request))

"""def specific_content(request, grade, subject, unit):
	error = False
	try:
		s = Subject.objects.get(name=subject)
		g = Grade.objects.get(name=grade)
		u = Unit.objects.get(letter=unit, grade=g, subject=s)
		experiments = Lecture.objects.filter(lecture_type='EXPERIMENT').order_by('cuasimodo_lecture_id')
		lectures = Lecture.objects.filter(lecture_type='LECTURE').order_by('cuasimodo_lecture_id')
		exercises = Exercise.objects.filter(unit=u, grade=g, unit__subject=s).order_by('cuasimodo_exercise_id')
		homeworks = Lecture.objects.filter(lecture_type='HOMEWORK').order_by('cuasimodo_lecture_id')
	except:
		error = True

	return render_to_response('contents.html',{'subject':s, 'unit':u, 'experiments':experiments,'lectures':lectures, 'exercises':exercises, 'homeworks':homeworks, 'error':error}, context_instance = RequestContext(request))"""

def specific_content(request, code, subject, unit, number):
	error = False
	try:
		print unit
		s = Subject.objects.get(name=subject)
		print '2'
		cr = ClassRoom.objects.get(pk=code)
		print cr.grade.name , ' grado de la clase'
		g = Grade.objects.get(pk=1)
		print  g.name + ' nombre grado'
		u = Unit.objects.get(letter='A', grade=g, subject=s)
		print '5'
		exercise = Exercise.objects.filter(unit=u, grade=g, unit__subject=s, cuasimodo_exercise_id=number)
		print '6'
	except:
		error = True
	return render_to_response('specific_content.html',{'subject':s, 'unit':u, 'exercise':exercise, 'error':error}, context_instance = RequestContext(request))


		