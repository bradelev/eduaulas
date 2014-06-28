from eduaulas import settings
from django.shortcuts import render
from student.models import Student
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.

def students_list(request,code):

	students = Student.objects.all()
	return render_to_response('studentsList.html',{'students':students}, context_instance = RequestContext(request))


def student_info(request,id):
	
	student = Student.objects.get(pk=id)
	if student.gender == 'FEMALE':
		student_gender = 'Femenino'
	else:
		student_gender = 'Masculino'
	return render_to_response('studentInfo.html',{'student':student, 'gender':student_gender}, context_instance = RequestContext(request))
	
