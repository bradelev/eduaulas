from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from student.models import Student
from configurations.models import Configuration
from classroom.models import  ClassRoom
from exercise.models import Unit, Exercise, Result, Area, Subject, Lecture
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
	var_areas = Area.objects.all()
	class_room = ClassRoom.objects.get(pk = code)
	return render_to_response('panel.html',{'areas':var_areas,'classroom':class_room}, context_instance = RequestContext(request))	

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
	except Area.DoesNotExist:
	        message = "No existe areas"
	result = simplejson.dumps({
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
			var_units = Unit.objects.filter(subject=s)
						
			for p in var_units:				
				dictionary_units[p.id] = {
					
					"name": p.name,
					"id": p.id								
					
				}
		
			type = "success"	
			result = simplejson.dumps({
			"dictionary_units":dictionary_units,
			"message":message,
			"type":type,
			}, cls = LazyEncoder)
			return HttpResponse(result, mimetype = 'application/javascript')

	except Unit.DoesNotExist:
		message = "No hay unidades"
	return HttpResponse(result, mimetype = 'application/javascript')


@login_required(login_url='/login/')
def list_students(request,code):

	dictionary_units_exercises={}
	message = ""
	type = "error"
	results_exist = 'no'
	students_exist = 'no'
	try:
		if request.POST:
			id_unit =request.POST['id_unit']
			var_unit = Unit.objects.get(pk=id_unit)	
			cl = ClassRoom.objects.get(pk=code)
			students = Student.objects.filter(class_room=cl)
			var_units_exercises = Exercise.objects.filter(unit=var_unit)
			matriz = []
			type = "success"
			i=0
			userid = request.user.id
			teacher_config = Configuration.objects.get(teacher=userid)
			for s in students:
				students_exist = 'yes'
				average = 0
				results_quantity = 0 
				total_points = 0 
				matriz.append([])
				matriz[i].append(s.id)
				matriz[i].append(s.name + ' '+ s.last_name)
									
				for j in var_units_exercises:
					var_results = Result.objects.filter(exercise=j, person=s)						
					if var_results.exists():
						results_exist = 'yes'
						for r in var_results:
							
							if r.points >= teacher_config.correct_points:
								matriz[i].append('<img src="/static/img/tickBien.png" >')
							if r.points <= teacher_config.incorrect_points:
								matriz[i].append('<img src="/static/img/tickMal.png" >')

							if (r.points < teacher_config.correct_points and r.points > teacher_config.incorrect_points):
								matriz[i].append('<img src="/static/img/tickMaso.png" >')

							results_quantity = results_quantity + 1	
							total_points += r.points
				

					else:
						matriz[i].append('')
				if results_quantity !=0:
					average = total_points / results_quantity
				if results_quantity >= teacher_config.minimum_quantity_exercise:
					print average  , s.name
					if average >= teacher_config.correct_points: 	
						matriz[i].append('green')
					if r.points <= teacher_config.incorrect_points:
						matriz[i].append('red')	
					if ((average < teacher_config.correct_points) and (average > teacher_config.incorrect_points)):	
						matriz[i].append('orange')	
				else:
					matriz[i].append('')		
				i = i + 1	
			
					
			for e in var_units_exercises:		
						
				dictionary_units_exercises[e.id] = {	

					"exercise_id": e.cuasimodo_exercise_id,
					"id": e.id,
					"img": e.thumb_img.url,			
					
				}	
				
			print matriz
	except Student.DoesNotExist:
		message = "No hay alumnos"
	result = simplejson.dumps({
			"dictionary_units_exercises":dictionary_units_exercises,
			"matriz":matriz,
			"results_exist":results_exist,
			"students_exist":students_exist,
			"message":message,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')

	
@login_required(login_url='/login/')
def load_suggestions_students(request,code):

	message = ""
	type = "error"
	
	try:
		userid = request.user.id
		teacher_config = Configuration.objects.get(teacher=userid)
		if request.POST:
			id_unit = request.POST['id_unit']
			var_unit = Unit.objects.get(pk=id_unit)	
			cl = ClassRoom.objects.get(pk=code)
			students = Student.objects.filter(class_room=cl)
			var_units_exercises = Exercise.objects.filter(unit=var_unit)
			matriz_suggestions_students = []
			type = "success"
			txt = ''
			i = 0
			for s in students:
				matriz_suggestions_students.append([])
				matriz_suggestions_students[i].append(s.id)
				matriz_suggestions_students[i].append(s.name + ' '+ s.last_name)
				txt = ''	
				exists_results = False			
				exists_exercise_for_suggest = False			
				for j in var_units_exercises:
					var_results = Result.objects.filter(exercise=j, person=s)						
					if var_results.exists():
						exists_results = True	
						for r in var_results:

							if r.points >= teacher_config.correct_points:

								good_exercises = Exercise.objects.get(pk=r.exercise.id).good_related_exercises.all()
								if good_exercises.exists():
									exists_exercise_for_suggest = True
									for g in good_exercises:														
										good_results =Result.objects.filter(exercise_id=g.id, person=s)									
																			
										if good_results.exists():		
																
											txt = '<h6>Ejercicios posterior al numero ' 
											matriz_suggestions_students[i].append(txt)
											txt = str(r.exercise.cuasimodo_exercise_id) + '</h6>'
											matriz_suggestions_students[i].append(txt)
											txt = 'Ej.' + '<a target="blank" href="/contenidos/ejercicio/'+ code + "/"+  str(g.id) +'">'+str(g.id) +" " +str(g.name)+'</a>'
											matriz_suggestions_students[i].append(txt)
											txt = ' Estado: Hecho' + '<br>'
											matriz_suggestions_students[i].append(txt)
										else:
											matriz_suggestions_students[i].append(txt)
											txt = 'Ej.' + '<a target="blank" href="/contenidos/ejercicio/'+ code + "/"+ str(g.id) + '">'+str(g.id) + " " +str(g.name)+'</a>'
											matriz_suggestions_students[i].append(txt)
											txt = ' Estado: Pendiente' + '<br>'
											matriz_suggestions_students[i].append(txt)
										
										
										txt = ''
										
							else:
								bad_exercises = Exercise.objects.get(pk=r.exercise.id).bad_related_exercises.all()
								if bad_exercises.exists():

									exists_exercise_for_suggest = True
									txt = '<h6>Ejercicios previo al numero '
									matriz_suggestions_students[i].append(txt)
									txt = str(r.exercise.cuasimodo_exercise_id) + '</h6>'		
								for b in bad_exercises:														
									bad_results =Result.objects.filter(exercise_id=b.id, person=s)

									if bad_results.exists():
										matriz_suggestions_students[i].append(txt)
										txt = 'Ej.' + '<a target="blank" href="/contenidos/ejercicio/'+ code + "/" + str(b.id) + '">'+str(b.id) +" " +str(b.name)+'</a>'
										matriz_suggestions_students[i].append(txt)
										txt = ' Estado: Hecho' + '<br>'
										matriz_suggestions_students[i].append(txt)
									else:

										matriz_suggestions_students[i].append(txt)
										txt = 'Ej.' + '<a target="blank" href="/contenidos/ejercicio/'+ code + "/"+ str(b.id) + '">'+str(b.id) + " "+ str(b.name)+'</a>'
										matriz_suggestions_students[i].append(txt)
										txt = ' Estado: Pendiente' + '<br>'
										matriz_suggestions_students[i].append(txt)
									txt = ''	
								lectures = Lecture.objects.get(pk=r.exercise.id).lectures.all()
								if lectures.exists():
									txt = '<h6>Lecturas sugeridas para el ejercicio ' +str(r.exercise.cuasimodo_exercise_id) + '</h6>'
									
										
									matriz_suggestions_students[i].append(txt)
									exists_exercise_for_suggest = True
									for l in lectures:
										txt =  str(l.name) + '<br>'
										matriz_suggestions_students[i].append(txt)
										#txt = 'Ej.' + '<a target="blank" href="/contenidos/ejercicio/'+str(b.id) +'">'+str(b.id)+'</a>'
										#matriz_suggestions_students[i].append(txt)

				
				if exists_results == False:	
					txt = 'El alumno aun no ha realizado ejercicios.'
					matriz_suggestions_students[i].append(txt)		
					txt = ''	
				if exists_exercise_for_suggest == False and exists_results == True:	
					txt = 'No hay sugerencias para mostrar.'
					matriz_suggestions_students[i].append(txt)		
					txt = ''		
				i = i + 1
													
								
			print(matriz_suggestions_students)
	except Student.DoesNotExist:
		message = "No hay alumnos"
	result = simplejson.dumps({
			"matriz_suggestions_students":matriz_suggestions_students,
			"message":message,
			"type":type,
		}, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')