from django.db import models
from student.models import Student
from classroom.models import Grade
from exercise.models import Unit, Exercise
from teacher.models import Teacher
from django.shortcuts import render_to_response
from django.template import RequestContext

def ingresar_datos(request):
	e = Student()
	e.name = 'Maria'
	e.last_name= 'Lacalle'
	e.save()

	e = Student()
	e.name = 'Federico'
	e.last_name= 'Gonzalez'
	e.save()

	e = Student()
	e.name = 'Jorge'
	e.last_name= 'Orecchia'
	e.save()

	e = Student()
	e.name = 'Lucia'
	e.last_name= 'Perez'
	e.save()

	e = Student()
	e.name = 'Agustina'
	e.last_name= 'Lopez'
	e.save()


	u= Unit()
	return render_to_response('index.html', context_instance = RequestContext(request))