from django.shortcuts import render_to_response
from django.template import RequestContext
from student.models import Student
from classroom.models import  ClassRoom
from exercise.models import Unit, Exercise, Result

# Create your views here.

def lista(request):
	units= Unit.objects.all()

	return render_to_response('panel.html',{'us':units}, context_instance = RequestContext(request))

def lista2(request,unit_id):
	var_unit = Unit.objects.get(pk=unit_id)
	cl = ClassRoom.objects.get(pk='efr5g')
	students = Student.objects.filter(class_room=cl)
	
	exercises = Exercise.objects.filter(unit=var_unit)
	#var_results= Result.objects.all()

	#var_results = Result.objects.all() 
	#for s in students:
	var_results = Result.objects.filter(student=students, exercise=exercises)
	#	for e in exercises:
	#		var_results = Result.objects.filter(id__in=[2,5,6,7,8]) 
			

	return render_to_response('panel.html',{'students':students,'ex':exercises, 'results': var_results }, context_instance = RequestContext(request))


#	render_to_response('index.html', context_instance = RequestContext(request))

#
#def crear(request):
#	render_to_response'index.html', context_instance = RequestContext(request))

#def compartir(request):
#	render_to_response('index.html', context_instance = RequestContext(request))

#def detalle(request, id):
#	render_to_response('index.html', context_instance = RequestContext(request))	
