from eduaulas import settings
from django.shortcuts import render
from student.models import Student
from exercise.models import Exercise, Result,Unit,Subject
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.


def ini(request,code):
	return render_to_response('studentsList.html',{'code':code}, context_instance = RequestContext(request))

def students_list(request):
	dictionary_students_profiles={}
	dictionary_subjects_students_average ={}
	dictionary_subjects ={}
	dictionary_students ={}
	type = "error"
	try:

		if request.POST:
			code =request.POST['code']
		students = Student.objects.all()
		print(code)
		for s in students:
			cont=0
			metacognitive_percentage= 0
			cognitive_percentage =0
			socio_affective_percentage=0
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
				dictionary_students_profiles [s.id]={		

						"metacognitive": average_metacognitive_percentage,
						"cognitive": average_cognitive_percentage,	
						"socio_affective":average_socio_affective_percentage
					}
		print(dictionary_students_profiles)	

		sub = Subject.objects.all()
				
		for s in sub:	
			dictionary_subjects[s.id]=	{

				"subject_name": s.name,
				"subject_id": s.id
			}					
			for st in students:
				dictionary_students[st.id] ={
					"name":st.name,
					"last_name": st.last_name

				}
				student_exercises_result= Result.objects.filter(student=st,exercise__unit__subject=s)
				cont1=0
				average=0
				points=0
				if student_exercises_result.exists():

					for r in student_exercises_result:				
						cont1 = cont1 + 1					
						points += r.points
					average = points/cont1
					indice= s.name + str(r.student.id)
					dictionary_subjects_students_average [indice]={		
						"subj":s.id,
						"student": r.student.id,
						"average": average*100				
					}
		type= "success"
	print(type)
	except Student.DoesNotExist:
	        message = "No hay alumnos"				
	result = simplejson.dumps({
                "dictionary_subjects":dictionary_subjects,
                "dictionary_students": dictionary_students,
                "dictionary_subjects_students_average":dictionary_subjects_students_average,
                "dictionary_students_profiles":dictionary_students_profiles,
                "code":code,
                "message":message,
                "type":type,
        }, cls = LazyEncoder)
	return HttpResponse(result, mimetype = 'application/javascript')
	




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
	return render_to_response('studentInfo.html',{'list_average':dictionary_subjects_average,'student':student, 'gender':student_gender,'socio_affective_percentage':average_socio_affective_percentage,'cognitive_percentage':average_cognitive_percentage, 'metacognitive_percentage':average_metacognitive_percentage}, context_instance = RequestContext(request))

	
	
