from django.shortcuts import render_to_response
from django.template import RequestContext
from student.models import Student
from exercise.models import Unit, Exercise

# Create your views here.

def lista(request):
	unit = Unit.objects.all()
	students = Student.objects.all()
	exercises = Exercise.objects.filter()
	return render_to_response('panel.html',{'students':students,'us': unit,'ex':exercises }, context_instance = RequestContext(request))
#	render_to_response('index.html', context_instance = RequestContext(request))

def crear(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def compartir(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def detalle(request, id):
	render_to_response('index.html', context_instance = RequestContext(request))	
