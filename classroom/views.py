from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
import random
from classroom.models import  ClassRoom



# Create your views here.

def classroom_list(request):


	return render_to_response('classroomAdmin.html', context_instance = RequestContext(request))


def classroom_add(request):
	generate_classroom_code()
	if request.POST:
		country =request.POST['country'] 
		department = request.POST['department']  
        schoolNumber= request.POST['schoolNumber'] 
        grade= request.POST['grade'] 
        className=request.POST['className'] 
        shift=request.POST['shift'] 
        
        c= ClassRoom()
        c.code=random.choice('AFcgoje67497368')
        c.class_letter=className
        c.shift=shift
        c.grade= grade
        c.school=schoolNumber

	return render_to_response('classroomAdd.html', context_instance = RequestContext(request))


def generate_classroom_code():

	code= random.choice('AFcgoje67497368')
	print(code,"randomico")
