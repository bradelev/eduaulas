from django.db import models
from student.models import Student
from django.shortcuts import render_to_response
from django.template import RequestContext

def ingresar_datos(request):
	e = Student()
	e.name = 'Thiago'
	e.last_name= 'Ivannov'
	e.save()
	return render_to_response('index.html', context_instance = RequestContext(request))