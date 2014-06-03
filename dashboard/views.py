from django.shortcuts import render_to_response
from django.template import RequestContext
from student.models import Student

# Create your views here.

def lista(request):
	
	students = Student.objects.all()
	return render_to_response('panel.html',{'students':students}, context_instance = RequestContext(request))
#	render_to_response('index.html', context_instance = RequestContext(request))

def crear(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def compartir(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def detalle(request, id):
	render_to_response('index.html', context_instance = RequestContext(request))	
