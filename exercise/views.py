from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from classroom.models import  ClassRoom, Grade
from exercise.models import Exercise, Lecture, Subject, Unit, Area,TeacherComments
from django.utils import simplejson
import json
from django.http import *
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from teacher.models import Teacher
import socket
from django.contrib.auth.models import User


# Create your views here.

class LazyEncoder(json.JSONEncoder):
	"""Encodes django's lazy i18n strings."""
    
   
	def default(self, obj):
	    if isinstance(obj, Promise):
	    	return force_unicode(obj)
	    return obj  

	
@login_required(login_url='/login/')
def ini(request,code):
	var_areas = Area.objects.all()
	class_room = ClassRoom.objects.get(pk = code)
	return render_to_response('contents.html',{'classroom':class_room,'areas':var_areas,'code':code}, context_instance = RequestContext(request))	

@login_required(login_url='/login/')
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
	result = json.dumps({
	                "dictionary_subjects":dictionary_subjects,
	                "code":code,
	                "message":message,
	                "type":type,
	        }, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')
	


@login_required(login_url='/login/')
def load_filters_unit(request,code):
	dictionary_units = {}
	message = ""
	type = "error"
	try:
		if request.POST:
			id_subject =request.POST['id_subject']			
			s = Subject.objects.get(pk=id_subject)
			c = ClassRoom.objects.get(code=code)
			var_units = Unit.objects.filter(subject=s, grade=c.grade)
			for p in var_units:				
				dictionary_units[p.id] = {
					"name": p.name,
					"id": p.id
				}
			type = "success"	
			result = json.dumps({
			"dictionary_units":dictionary_units,
			"message":message,
			"type":type,
			}, cls = LazyEncoder)
			return HttpResponse(result, mimetype = 'application/javascript')
	except Unit.DoesNotExist:
		message = "No hay unidades"
	except:
		message = "Otro error"
	return HttpResponse(result, mimetype = 'application/javascript')


@login_required(login_url='/login/')
def list_contents(request,code):
	message = ""
	type = "error"
	result = ""
	dictionary_experiments = {}
 	dictionary_lectures = {}
 	dictionary_exercises = {}
 	dictionary_homeworks = {}
	try:
		if request.POST:
			id_unit = request.POST['id_unit']
			u = Unit.objects.get(pk=id_unit)			
			#cl = ClassRoom.objects.get(pk=code)
			g = u.grade
			s = u.subject
			
			experiments = Lecture.objects.filter(lecture_type='EXPERIMENT', unit=u, grade=g, unit__subject=s).order_by('cuasimodo_lecture_id')
			lectures = Lecture.objects.filter(lecture_type='LECTURE', unit=u, grade=g, unit__subject=s).order_by('cuasimodo_lecture_id')
			exercises = Exercise.objects.filter(unit=u, grade=g, unit__subject=s).order_by('cuasimodo_exercise_id')
			homeworks = Lecture.objects.filter(lecture_type='HOMEWORK', unit=u, grade=g, unit__subject=s).order_by('cuasimodo_lecture_id')
			for e in experiments:
				dictionary_experiments[e.id] = {
					'id':e.id,
					"id_cuasimodo": e.cuasimodo_lecture_id,
					"guia": e.teacher_guide,
					"lecture_type": "Experimento",
					"img": e.img.url
				}
			for l in lectures:
				dictionary_lectures[l.id] = {
					'id':l.id,	
					"id_cuasimodo": l.cuasimodo_lecture_id,
					"guia": l.teacher_guide,
					"lecture_type": "Lectura",
					"img": l.img.url
				}
			for e in exercises:
				dictionary_exercises[e.id] = {
					'id':e.id,
					"id_cuasimodo": e.cuasimodo_exercise_id,
					"guia": e.teacher_guide,
					"lecture_type": "Ejercicio",
					"img": e.img.url,
					"name":e.name,
				}
			for h in homeworks:
				dictionary_homeworks[h.id] = {
					'id':h.id,
					"id_cuasimodo": h.cuasimodo_lecture_id,
					"guia": h.teacher_guide,
					"lecture_type": "Tarea",
					"img": h.img.url
				}
		type = "success"
		message = "Todo bien"
	except ClassRoom.DoesNotExist:
	        message = "No hay aulas"
	result = json.dumps({
	        "dictionary_experiments":dictionary_experiments,
			"dictionary_lectures":dictionary_lectures,
			"dictionary_exercises":dictionary_exercises,
			"dictionary_homeworks":dictionary_homeworks,
			"subject":s.name,
			"unit_letter":u.letter,
			"unit_name":u.name,
            "message":message,
            "type":type,
	        }, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')


@login_required(login_url='/login/')
def send_comment(request,code):
    message = ""
    type = "error"
    try:
        if request.POST:
			
			try:
				userid = request.user.id
				print userid , 'usuario'
				t = Teacher.objects.get(user=userid)
			except:
				message = "no se encontro maestro"
				print message
			txt_comment = request.POST['comment']
			print txt_comment, 'cometario'
			print t.name
			try:
				c = TeacherComments(teacher=t)
				print 'guarde'
				c.comments = txt_comment
				c.save()
			except:
				message = "No se pude guardar el comentario"
				print message

			

			type = "success"
    except:
        print('entre a la execpcion')
        message = "No hay docente"

    result = json.dumps({            
            "message":message,
            "type":type,
        }, cls = LazyEncoder)
    return HttpResponse(result, content_type = 'application/javascript')	





@login_required(login_url='/login/')
def specific_content(request, grade, subject, unit, number):
	error = False
	try:
		s = Subject.objects.get(name=subject)
		g = Grade.objects.filter(name=grade)
		u = Unit.objects.get(letter=unit, grade=g, subject=s)
		exercise = Exercise.objects.filter(unit=u, grade=g, unit__subject=s, cuasimodo_exercise_id=number)
	except:
		error = True
	return render_to_response('specific_content.html',{'subject':s, 'unit':u, 'exercise':exercise, 'error':error}, context_instance = RequestContext(request))

@login_required(login_url='/login/')
def specific_exercise_id(request,code,id):
	error = False
	try:
		exercise = Exercise.objects.get(pk=id)
		s = exercise.unit.subject
		g = exercise.grade
		u = exercise.unit

	except Exercise.DoesNotExist:
		print "no encontro ejercicio"
		error = True
	return render_to_response('specific_content.html',{'subject':s, 'unit':u, 'exercise':exercise, 'error':error}, context_instance = RequestContext(request))

@login_required(login_url='/login/')
def specific_lecture_id(request,code,id):
	error = False
	try:
		lecture = Lecture.objects.get(pk=id)
		s = lecture.unit.subject
		g = lecture.grade
		u = lecture.unit

	except Exercise.DoesNotExist:
		print "no encontro ejercicio"
		error = True
	return render_to_response('specific_lecture.html',{'subject':s, 'unit':u, 'lecture':lecture, 'error':error}, context_instance = RequestContext(request))	


		