from eduaulas import settings
from django.shortcuts import render
from student.models import Student
from exercise.models import Exercise, Result,Unit,Subject
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.

def students_list(request,code):
	dictionary_students_profiles={}
	dictionary_subjects_students_average ={}
	metacognitive_percentage= 0
	cognitive_percentage =0
	socio_affective_percentage=0
	
	students = Student.objects.all()
	for s in students:
		cont=0
		students_profiles= Result.objects.filter(student=s)
		if students_profiles.exists():
			for p in students_profiles:
				cont = cont + 1
				metacognitive_percentage += p.exercise.metacognitive_percentage
				cognitive_percentage += p.exercise.cognitive_percentage
				socio_affective_percentage += p.exercise.socio_affective_percentage

			average_metacognitive_percentage= metacognitive_percentage/cont
			average_cognitive_percentage= cognitive_percentage/cont
			average_socio_affective_percentage= socio_affective_percentage/cont
			dictionary_students_profiles [s.name]={		

					"metacognitive": average_metacognitive_percentage,
					"cognitive": average_cognitive_percentage,	
					"socio_affective":average_socio_affective_percentage
				}
			print(dictionary_students_profiles)	

	sub = Subject.objects.all()
			
	for s in sub:			
		points=0
		average=0
		for st in students:
			student_exercises_result= Result.objects.filter(student=st,exercise__unit__subject=s)
			cont1=0
			if student_exercises_result.exists():
				for r in student_exercises_result:
				
					cont1 = cont1 + 1
					
					points += r.points
				average = points/cont1
				
			dictionary_subjects_students_average [s.name]={		

				#"subject": s.name,
				"average": average*100+ 1				
			}
							
	print(dictionary_subjects_students_average)		
	return render_to_response('studentsList.html',{'students':students}, context_instance = RequestContext(request))




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
			student_exercises_result= Result.objects.filter(student=student,exercise__unit__subject=s)
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


		student_profiles= Result.objects.filter(student=student)

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
	return render_to_response('studentInfo.html',{'list_average':dictionary_subjects_average,'student':student, 'gender':student_gender,'socio_affective_percentage':average_socio_affective_percentage,'cognitive_percentage':average_cognitive_percentage, 'metacognitive_percentage':average_metacognitive_percentage}, context_instance = RequestContext(request))

	
	
