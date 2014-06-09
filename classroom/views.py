from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
import random
from classroom.models import  ClassRoom, Grade
from location.models import School, Country, Department



# Create your views here.

def classroom_list(request):


	return render_to_response('classroomAdmin.html', context_instance = RequestContext(request))

def classroom_list(request):
        classrooms = ClassRoom.objects.all()
        """dictionary_classrooms = {}
        message = ""
        type = "error"
        try:
                classrooms = ClassRoom.objects.all()
                type = "success"
                for x in students:                              
                        dictionary_classrooms[x.code] = {
                                
                                "code": x.code,
                                "class_letter": x.class_letter
                                
                        }
                
        except ClassRoom.DoesNotExist:
                message = "No hay aulas"
        result = simplejson.dumps({
                        "dictionary_classrooms":dictionary_classrooms,
                        "message":message,
                        "type":type,
                }, cls = LazyEncoder)
        return HttpResponse(result, mimetype = 'application/javascript')"""
        
        return render_to_response('classroomList.html',{'classrooms':classrooms}, context_instance = RequestContext(request))
       

def classroom_add(request):
      
	if request.POST:

		country =request.POST['country'] 
		department = request.POST['department']  
                schoolNumber= request.POST['schoolNumber'] 
                grade= request.POST['grade'] 
                className=request.POST['className'] 
                shift=request.POST['shift']               
                c= ClassRoom()
                c.code = generate_classroom_code()
                c.class_letter = className
                c.shift = shift
                g = Grade.objects.get(name=grade)
                c.grade=g
                s= School.objects.get(number=schoolNumber)
                c.school=s
                c.save()
        else:
               countrys = Country.objects.all()
               departments = Department.objects.all()        
               schools = School.objects.all()
               grades= Grade.objects.all()
               return render_to_response('classroomAdd.html',{'countrys':countrys, 'departments': departments, 'schools': schools,'grades': grades}, context_instance = RequestContext(request))


	return render_to_response('classroomAdd.html', context_instance = RequestContext(request))


def generate_classroom_code():

        code=''
        for x in xrange(1,5):                
        	code+= random.choice('AFcgoje67497368')
        return code
	
