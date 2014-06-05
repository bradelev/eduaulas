from django.db import models
from student.models import Student
from classroom.models import Grade, ClassRoom
from exercise.models import Unit, Exercise
from teacher.models import Teacher
from django.shortcuts import render_to_response
from django.template import RequestContext

def ingresar_datos(request):
	
	c = ClassRoom.objects.get(pk='efr5g')

	e = Student()
	e.name = 'Maria'
	e.last_name= 'Lacalle'
	e.class_room=c
	e.save()

	e = Student()
	e.name = 'Federico'
	e.last_name= 'Gonzalez'
	e.class_room=c
	e.save()

	e = Student()
	e.name = 'Jorge'
	e.last_name= 'Orecchia'
	e.class_room=c
	e.save()

	e = Student()
	e.name = 'Lucia'
	e.last_name= 'Perez'
	e.class_room=c
	e.save()

	e = Student()
	e.name = 'Agustina'
	e.last_name= 'Lopez'
	e.class_room=c
	e.save()


	
	
	return render_to_response('index.html', context_instance = RequestContext(request))