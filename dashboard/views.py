from django.shortcuts import render_to_response
from django.template import RequestContext
from student.models import Student

# Create your views here.

def lista(request):
	
	e = Student()
	e.name = 'Thiago'
	e.last_name= 'Ivannov'
	e.save()
	students = Student.objects.all()
	return render_to_response('index.html',{'students':students}, context_instance = RequestContext(request))
#	render_to_response('index.html', context_instance = RequestContext(request))

def crear(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def compartir(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def detalle(request, id):
	render_to_response('index.html', context_instance = RequestContext(request))	
