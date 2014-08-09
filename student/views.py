from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from eduaulas import settings
from django.shortcuts import render
from student.models import Student, Person
from exercise.models import Exercise, Result,Unit,Subject
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
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

@login_required(login_url='/login/')
def ini(request,code):


	return render_to_response('students_list.html',{"code":code}, context_instance = RequestContext(request))

@login_required(login_url='/login/')
def students_info(request,code):
	message = ""
	type = "error"
	students = Student.objects.filter(class_room=code)
	matriz = []
	i=0
	average=0
	points=0
	try:
		for s in students:
			metacognitive_percentage= 0
			cognitive_percentage =0
			socio_affective_percentage=0
			average_metacognitive_percentage=0
			average_cognitive_percentage=0
			average_socio_affective_percentage=0
			cont=0
			
			students_results= Result.objects.filter(person=s)
			matriz.append([])
			matriz[i].append(s.id)
			matriz[i].append(s.name + ' '+ s.last_name)
			if students_results.exists():
				for p in students_results:
					cont = cont + 1
					metacognitive_percentage += p.exercise.metacognitive_percentage
					cognitive_percentage += p.exercise.cognitive_percentage
					socio_affective_percentage += p.exercise.socio_affective_percentage
					points += p.points
				average_points = points/cont
				average_metacognitive_percentage= (metacognitive_percentage/cont)*average_points
				matriz[i].append(average_metacognitive_percentage)
			
				average_cognitive_percentage= (cognitive_percentage/cont)*average_points
				matriz[i].append(average_cognitive_percentage)
				average_socio_affective_percentage= (socio_affective_percentage/cont)*average_points
				matriz[i].append(average_socio_affective_percentage)
				
				matriz[i].append(average_points)
				

			else:
				matriz[i].append('')
				matriz[i].append('')
				matriz[i].append('')
				matriz[i].append('')
			i = i + 1
			print(matriz)
			type = "success"
		   
	except Student.DoesNotExist:
		message = "No hay alumnos"
	result = simplejson.dumps({
			"matriz":matriz,
			"message":message,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')




@login_required(login_url='/login/')
def student_info(request,id):
	
	dictionary_subjects_average={}
	student = Student.objects.get(pk=id)

	if student.gender == 'FEMALE':
		student_gender = 'Femenino'
	else:
		student_gender = 'Masculino'
	try:

		cont=0
		metacognitive_percentage= 0
		cognitive_percentage =0
		socio_affective_percentage=0
		sub = Subject.objects.all()
		
		
		for s in sub:
			
			points=0
			average=0
			student_exercises_result= Result.objects.filter(person=student,exercise__unit__subject=s)
			cont1=0
			if student_exercises_result.exists():
				for r in student_exercises_result:
				
					cont1 = cont1 + 1
					
					points += r.points
				average = points/cont1
				
			dictionary_subjects_average [s.name]={		

				#"subject": s.name,
				"average": average*100+ 1				
			}
								
		print(dictionary_subjects_average)


		student_profiles= Result.objects.filter(person=student)

		for p in student_profiles:
			cont = cont + 1
			metacognitive_percentage += p.exercise.metacognitive_percentage
			cognitive_percentage += p.exercise.cognitive_percentage
			socio_affective_percentage += p.exercise.socio_affective_percentage

		average_metacognitive_percentage= metacognitive_percentage/cont
		average_cognitive_percentage= cognitive_percentage/cont
		average_socio_affective_percentage= socio_affective_percentage/cont


	except Result.DoesNotExist:
	        message = "El alumno no tiene ejercicios"
	return render_to_response('student_info.html',{'list_average':dictionary_subjects_average,'student':student, 'gender':student_gender,'socio_affective_percentage':average_socio_affective_percentage,'cognitive_percentage':average_cognitive_percentage, 'metacognitive_percentage':average_metacognitive_percentage}, context_instance = RequestContext(request))

	
@login_required(login_url='/login/')	
def stats_by_learning_profiles(request,code):
	students = Student.objects.filter(class_room=code)
	
	points=0
	metacognitive_percentage= 0
	cognitive_percentage =0
	socio_affective_percentage=0		
	average_metacognitive_percentage=0
	average_cognitive_percentage=0
	average_socio_affective_percentage=0
	cont=0		
	students_results= Result.objects.filter(person__student__class_room__code=code)

	if students_results.exists():
		for p in students_results:
			cont = cont + 1
			metacognitive_percentage += p.exercise.metacognitive_percentage
			cognitive_percentage += p.exercise.cognitive_percentage
			socio_affective_percentage += p.exercise.socio_affective_percentage
			points += p.points
		if cont <> 0:	
			average_points = points/cont
			average_metacognitive_percentage = (metacognitive_percentage*average_points)/cont	
			average_cognitive_percentage = (cognitive_percentage*average_points)/cont
			average_socio_affective_percentage = (socio_affective_percentage*average_points)/cont
		print average_metacognitive_percentage , 'average_metacognitive_percentage'
		print average_cognitive_percentage, 'average_cognitive_percentage'
		print average_socio_affective_percentage, 'average_socio_affective_percentage'

	return render_to_response('stats_by_learning_profiles.html',{"code":code,"cognitive_percentage":average_cognitive_percentage,"metacognitive_percentage":average_metacognitive_percentage,"socio_affective_percentage":average_socio_affective_percentage}, context_instance = RequestContext(request))


@login_required(login_url='/login/')
def ini_stats_by_topics(request,code):

	return render_to_response('stats_by_topic.html',{'code':code}, context_instance = RequestContext(request))

@login_required(login_url='/login/')
def stats_by_topics(request,code):
	
	message = ""
	type = "error"
	subjects = Subject.objects.all()
	matriz = []
	i=0
	points=0
	average_points_subject=0	
	cont=0	
	try:
		for sb in subjects:
			average_points_subject=0
			points=0
			matriz.append([])
			students_results_sub = Result.objects.filter(exercise__unit__subject__id=sb.id,person__student__class_room__code=code)		
							
			matriz[i].append(sb.name)			
			for r in students_results_sub:
				print r.exercise.unit.subject.id 
				cont = cont + 1 				
				points += r.points
			
			if cont <>0:		
				average_points_subject = points/cont
			matriz[i].append(average_points_subject)
			i = i + 1

		type = "success"	
		print(matriz)

	except Student.DoesNotExist:
		message = "No hay alumnos"
	result = simplejson.dumps({
			"matriz":matriz,
			"message":message,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')

"""
students = Student.objects.filter(class_room=code)
	
	points=0
	average_metacognitive_percentage_class=0
	average_cognitive_percentage_class=0
	average_socio_affective_percentage_class=0		
	average_metacognitive_percentage=0
	average_cognitive_percentage=0
	average_socio_affective_percentage=0
	for s in students:
		metacognitive_percentage= 0
		cognitive_percentage =0
		socio_affective_percentage=0		
		cont=0		
		students_results= Result.objects.filter(person=s)

		if students_results.exists():
			for p in students_results:
				cont = cont + 1
				metacognitive_percentage += p.exercise.metacognitive_percentage
				cognitive_percentage += p.exercise.cognitive_percentage
				socio_affective_percentage += p.exercise.socio_affective_percentage
				points += p.points
			average_points = points/cont
			average_metacognitive_percentage = (metacognitive_percentage/cont)*average_points		
			average_cognitive_percentage = (cognitive_percentage/cont)*average_points
			average_socio_affective_percentage = (socio_affective_percentage/cont)*average_points

	average_metacognitive_percentage_class += average_metacognitive_percentage
	average_cognitive_percentage_class += average_cognitive_percentage
	average_socio_affective_percentage_class += average_socio_affective_percentage	
"""
