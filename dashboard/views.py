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
	var_subjects = Subject.objects.all()
	var_units = Unit.objects.all()

	return render_to_response('panel2.html',{'areas':var_areas,'subjects':var_subjects, 'units':var_units }, context_instance = RequestContext(request))

	


def list_students(request):
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
		for x in dictionary_students:				
			dictionary_students[x.id] = {
				
				"name": name,
				
			}
		
	except Student.DoesNotExist:
		message = "No hay alumnos"
	result = simplejson.dumps({
			"dictionary_students":dictionary_students,
			"message":message,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')

	#return render_to_response('panel2.html',{'students':students,'ex':exercises, 'results': var_results }, context_instance = RequestContext(request))


#	render_to_response('index.html', context_instance = RequestContext(request))

#


def compartir(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def detalle(request, id):
	render_to_response('index.html', context_instance = RequestContext(request))	
