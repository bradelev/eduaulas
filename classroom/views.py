from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
import random
from classroom.models import  ClassRoom, Grade
from location.models import School, Country, Department
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

def ini(request):


	return render_to_response('classroomList.html', context_instance = RequestContext(request))

def edit_classroom(request):
        dictionary_school = {}
        dictionary_classroom = {}
        message = ""
        type = "error"
        
        try:
            if request.POST:
                
                code =request.POST['code'] 
                classroom = ClassRoom.objects.get(pk=code) 
                s = classroom.school.id           
                sch = School.objects.get(pk=s)
                type = "success"
                dictionary_classroom[classroom.code] = {
                           
                        "country_id": classroom.school.department.country.id,
                        "department_id":classroom.school.department.id,                                        
                        "shift": classroom.shift,
                        "class_letter": classroom.class_letter,
                        "grade_id":classroom.grade.id,
                        "school_id": classroom.school.id,
                        }

                
        except ClassRoom.DoesNotExist:
                message = "No hay aulas"
        result = simplejson.dumps({
                        "dictionary_classroom":dictionary_classroom,
                        #"dictionary_school":dictionary_school,
                        "message":message,
                        "type":type,
                }, cls = LazyEncoder)
        return HttpResponse(result, mimetype = 'application/javascript')

def classroom_list(request):
       # classrooms = ClassRoom.objects.all()
        dictionary_classrooms = {}
        message = ""
        type = "error"
        try:
                classrooms = ClassRoom.objects.all()
                type = "success"
                for x in classrooms:                              
                        dictionary_classrooms[x.code] = {
                                
                                "code": x.code,
                                "shift": x.shift,
                                "class_letter": x.class_letter,
                                "grade":x.grade.name,
                                "school": x.school.name,

                                
                        }
                
        except ClassRoom.DoesNotExist:
                message = "No hay aulas"
        result = simplejson.dumps({
                        "dictionary_classrooms":dictionary_classrooms,
                        "message":message,
                        "type":type,
                }, cls = LazyEncoder)
        return HttpResponse(result, mimetype = 'application/javascript')
        
       # return render_to_response('classroomList.html',{'classrooms':classrooms}, context_instance = RequestContext(request))
       

def classroom_save(request):
   
    message = ""
    type = "error"
    print('entre al save')
    try:

        if request.POST:
            editing_classroom =request.POST['editing_classroom'] 
            print(editing_classroom)
            country =request.POST['select_country'] 
            department = request.POST['select_department']  
            school= request.POST['select_school'] 
            grade= request.POST['select_grade'] 
            className=request.POST['class_name'] 
            shift=request.POST['select_shift']               
            c= ClassRoom()
            c.code = generate_classroom_code()
            c.class_letter = className
            c.shift = shift
            g = Grade.objects.get(pk=grade)
            c.grade=g
            s= School.objects.get(pk=school)
            c.school=s
            c.save()
            type = "success"
    except ClassRoom.DoesNotExist:
        print('entre a la execpcion')
        message = "No hay alumnos"

    result = simplejson.dumps({            
            "message":message,
            "type":type,
        }, cls = LazyEncoder)
    return HttpResponse(result, mimetype = 'application/javascript')
  
 
	


def load_classroom_form(request):

    dictionary_countrys = {}
    dictionary_schools = {}
    dictionary_grades = {}
    
    
    message = ""
    type = "error"
    try:
        
        countrys = Country.objects.all()   
        schools = School.objects.all()
        grades= Grade.objects.all()
        type = "success"
              
        for y in countrys:                
            dictionary_countrys[y.id] = {
                
                "name": y.name,
                "id": y.id                               
            }
        
        for s in schools:                
            dictionary_schools[s.id] = {
                
                "name": s.name,
                "id": s.id                               
            }
        for g in grades:                
            dictionary_grades[g.id] = {
                
                "name": g.name,
                "id": g.id                               
            }
        result = simplejson.dumps({
        "dictionary_countrys":dictionary_countrys,
        "dictionary_schools":dictionary_schools,
        "dictionary_grades":dictionary_grades,
        "message":message,
        "type":type,
        }, cls = LazyEncoder)
        return HttpResponse(result, mimetype = 'application/javascript')
            #return render_to_response('classroomList.html',{'countrys':countrys, 'departments': departments, 'schools': schools,'grades': grades}, context_instance = RequestContext(request))
    except Student.DoesNotExist:
        message = "No hay alumnos"
    
    return HttpResponse(result, mimetype = 'application/javascript')

def load_departments(request):

    dictionary_departments = {}
    
    message = ""
    type = "error"
    try:
        if request.POST:
            print('hola post')            
            id_country =request.POST['id_country']
            print('hola 2',id_country)
            c = Country.objects.get(pk=id_country)
            print('hola 3')
            departments = Department.objects.filter(country=c)  
            print('hola 4')      
            
            type = "success"

            for d in departments:                
                dictionary_departments[d.id] = {
                    
                    "name": d.name,
                    "id": d.id                               
                }

        result = simplejson.dumps({
        "dictionary_departments":dictionary_departments,
        "message":message,
        "type":type,
        }, cls = LazyEncoder)
        return HttpResponse(result, mimetype = 'application/javascript')
            #return render_to_response('classroomList.html',{'countrys':countrys, 'departments': departments, 'schools': schools,'grades': grades}, context_instance = RequestContext(request))
    except Student.DoesNotExist:
        message = "No hay departments"
    
    return HttpResponse(result, mimetype = 'application/javascript')


def generate_classroom_code():

        code=''
        for x in xrange(1,5):                
        	code+= random.choice('AFcgoje67497368')
        return code
	
