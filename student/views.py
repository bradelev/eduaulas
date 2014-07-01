from eduaulas import settings
from django.shortcuts import render
from student.models import Student
from exercise.models import Exercise, Result,Unit,Subject
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.

def students_list(request,code):

	students = Student.objects.all()
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
		student_exercises_result= Result.objects.filter(student=student)
		for r in student_exercises_result:
			cont = cont + 1
			metacognitive_percentage += r.exercise.metacognitive_percentage
			cognitive_percentage += r.exercise.cognitive_percentage
			socio_affective_percentage += r.exercise.socio_affective_percentage

		average_metacognitive_percentage= metacognitive_percentage/cont
		average_cognitive_percentage= cognitive_percentage/ cont
		average_socio_affective_percentage= socio_affective_percentage/cont

		#	
		"""
		for r in student_exercises_result:
			dictionary_subjects_average [r.exercise.unit.subject.id]= {

				"subject": r.exercise.unit.subject.id,
				#av +=r.points
				#"average": r.points
				
			}
		for p in dictionary_subjects_average.iterkeys():
			print(p)
			for r in student_exercises_result:
				print(r.exercise.unit.subject.id)
				if r.exercise.unit.subject.id == p:
					average += r.points
					print(average)

		#print(rs)

		print(dictionary_subjects_average)
			#subject_list.append(r.exercise.unit.subject.id)"""
						
						

		#print('Materia',subject_list)
		#print('promedio',average_by_subject)
	except Result.DoesNotExist:
	        message = "El alumno no tiene ejercicios"
	return render_to_response('studentInfo.html',{'student':student, 'gender':student_gender, 'metacognitive_percentage':average_metacognitive_percentage}, context_instance = RequestContext(request))
	
	
	#average_by_subject = 
	
	
