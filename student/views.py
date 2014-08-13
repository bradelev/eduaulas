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
import datetime
from configurations.models import Configuration
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
	quantity_students = 0
	try:
		for s in students:
			quantity_students = quantity_students + 1
			metacognitive_percentage= 0
			cognitive_percentage =0
			socio_affective_percentage=0
			average_metacognitive_percentage=0
			average_cognitive_percentage=0
			average_socio_affective_percentage=0
			quantity_results=0
			points=0
			students_results= Result.objects.filter(person=s)
			matriz.append([])
			matriz[i].append(s.id)
			matriz[i].append(s.name + ' '+ s.last_name)
			if students_results.exists():
				for p in students_results:
					quantity_results = quantity_results + 1
					metacognitive_percentage += p.exercise.metacognitive_percentage * p.points
					cognitive_percentage += p.exercise.cognitive_percentage * p.points
					socio_affective_percentage += p.exercise.socio_affective_percentage * p.points
					points += p.points

				if quantity_results != 0:
					average_points = (points/quantity_results)*100					
					average_metacognitive_percentage= metacognitive_percentage/quantity_results
					matriz[i].append(round(average_metacognitive_percentage,1))					
					average_cognitive_percentage= cognitive_percentage/quantity_results
					matriz[i].append(round(average_cognitive_percentage,1))
					average_socio_affective_percentage= socio_affective_percentage/quantity_results
					matriz[i].append(round(average_socio_affective_percentage,1))						
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
			"quantity_results":quantity_results,
			"quantity_students":quantity_students,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')




@login_required(login_url='/login/')
def student_info(request,code,id):
	years = ''

	dictionary_subjects_average={}
	student = Student.objects.get(pk=id)
	if not (student.date_of_birth is None):
		diff = (datetime.date.today() - student.date_of_birth).days
		years = str(int(diff/365))

	if student.gender == '1':
		student_gender = 'Femenino'
	else:
		student_gender = 'Masculino'
	try:
		userid = request.user.id
		teacher_config = Configuration.objects.get(teacher=userid)
		quantity_results = 0
		metacognitive_percentage = 0
		cognitive_percentage = 0
		socio_affective_percentage = 0
		sub = Subject.objects.all()
		average_metacognitive_percentage = 0
		average_cognitive_percentage = 0
		average_socio_affective_percentage = 0
		
		for s in sub:			
			points = 0
			average = 0
			student_exercises_result = Result.objects.filter(person=student,exercise__unit__subject=s)
			cont1 = 0
			if student_exercises_result.exists():
				for r in student_exercises_result:
				
					cont1 = cont1 + 1					
					points += r.points
				if cont1 != 0:	
					average = points/cont1
				
			dictionary_subjects_average [s.name]={		

				"average": average * 100 + 1,
				"incorrect_points":teacher_config.incorrect_points * 100,				
				"correct_points":teacher_config.correct_points * 100,				
			}
								
		print dictionary_subjects_average	
		student_results= Result.objects.filter(person=student)

		for r in student_results:
			quantity_results = quantity_results + 1
			metacognitive_percentage += (r.exercise.metacognitive_percentage * r.points) + 1
			cognitive_percentage += (r.exercise.cognitive_percentage * r.points) + 1
			socio_affective_percentage += (r.exercise.socio_affective_percentage * r.points) +1

		if quantity_results !=0:	
			average_metacognitive_percentage= metacognitive_percentage/quantity_results
			average_cognitive_percentage= cognitive_percentage/quantity_results
			average_socio_affective_percentage= socio_affective_percentage/quantity_results


	except Result.DoesNotExist:
	        message = "El alumno no tiene ejercicios"
	return render_to_response('student_info.html',{"code":code,"student_results":student_results,"quantity_results":quantity_results,'list_average':dictionary_subjects_average,'years':years,'student':student, 'gender':student_gender,'socio_affective_percentage':average_socio_affective_percentage,'cognitive_percentage':average_cognitive_percentage, 'metacognitive_percentage':average_metacognitive_percentage}, context_instance = RequestContext(request))

	
@login_required(login_url='/login/')	
def stats_by_learning_profiles(request,code):

	quantity_students = 0
	metacognitive_percentage= 0
	cognitive_percentage =0
	socio_affective_percentage=0		
	average_metacognitive_percentage=0
	average_cognitive_percentage=0
	average_socio_affective_percentage=0
	quantity_results=0		
	students_results= Result.objects.filter(person__student__class_room__code=code)
	#students = Result.objects.filter(person__student__class_room__code=code).distinct()
	#print len(students)

	#students = Student.objects.filter(class_room=code,)


	if students_results.exists():
		for p in students_results:
			quantity_results = quantity_results + 1
			metacognitive_percentage += p.exercise.metacognitive_percentage * p.points
			cognitive_percentage += p.exercise.cognitive_percentage * p.points
			socio_affective_percentage += p.exercise.socio_affective_percentage * p.points
			
		if quantity_results != 0:	
			
			average_metacognitive_percentage = (metacognitive_percentage/quantity_results)+1	
			average_cognitive_percentage = (cognitive_percentage /quantity_results) +1
			average_socio_affective_percentage = (socio_affective_percentage/quantity_results)+1
		

	return render_to_response('stats_by_learning_profiles.html',{"quantity_students":quantity_students,"quantity_results":quantity_results,"code":code,"cognitive_percentage":average_cognitive_percentage,"metacognitive_percentage":average_metacognitive_percentage,"socio_affective_percentage":average_socio_affective_percentage}, context_instance = RequestContext(request))




@login_required(login_url='/login/')
def stats_by_topics(request,code):
	dictionary_subjects_average ={}
	message = ""
	type = "error"
	subjects = Subject.objects.all()
	i=0
	points=0
	average_points_subject=0	
	quantity_results = 0	
	quantity_results_subject = 0	
	try:
		for sb in subjects:
			average_points_subject=0
			points=0
			quantity_results_subject = 0
			students_results_sub = Result.objects.filter(exercise__unit__subject__id=sb.id,person__student__class_room__code=code)		
							
			for r in students_results_sub:
				quantity_results = quantity_results + 1 			
				quantity_results_subject = quantity_results_subject +1	
				points += r.points
			
			if quantity_results != 0:		
				average_points_subject = points/quantity_results_subject

			dictionary_subjects_average [sb.name]={		

				"average": average_points_subject * 100 +1 ,
				"quantity_results_subject": quantity_results_subject 				
			}

		type = "success"	
		
	except Student.DoesNotExist:
		message = "No hay alumnos"
	return render_to_response('stats_by_topic.html',{'code':code,'dictionary_subjects_average':dictionary_subjects_average}, context_instance = RequestContext(request))


