from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
import random
import string
from classroom.models import  ClassRoom, Grade
from location.models import School, Country, Department
#from django.utils import json
from django.utils import simplejson
from django.http import *
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.views.decorators.csrf import ensure_csrf_cookie
from configurations.models import Configuration
from teacher.models import Teacher
#from django.http import Http500

# Create your views here 
class LazyEncoder(simplejson.JSONEncoder):
	"""Encodes django's lazy i18n strings."""
    
   
	def default(self, obj):
	    if isinstance(obj, Promise):
	    	return force_unicode(obj)
	    return obj  

@login_required(login_url='/login/')
def ini_redirect(request):
    return HttpResponseRedirect("/aulas/lista/")

@login_required(login_url='/login/')
def ini(request):
    try:
        userid = request.user.id
        teacher = Teacher.objects.get(user=userid)
        teacher_config = Configuration.objects.get(teacher=teacher.id)
       
    except:
        message="Debe loguearse como un maestro"
        return render_to_response('500.html',{"message":message}, context_instance = RequestContext(request))

    return render_to_response('classroom_list.html',{"teacher":teacher, "conf":teacher_config}, context_instance = RequestContext(request))

@login_required(login_url='/login/')
def load_classroom(request):
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
                        "code_class":classroom.code,
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

@login_required(login_url='/login/')
def classroom_list(request):

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
        
       

@login_required(login_url='/login/')
def classroom_save_add(request):
    print('entre al save')
    message = ""
    type = "error"
    
    try:
        if request.is_ajax():           
            if request.method == 'POST':                
                country =request.POST['select_country']                       
                department = request.POST['select_department']             
                school= request.POST['select_school']         
                grade= request.POST['select_grade'] 
                className=request.POST['class_name']           
                shift=request.POST['select_shift'] 

                c= ClassRoom()
                code = generate_classroom_code()
                print code, 'code'
                c.code= code
                c.class_letter = className
                c.shift = shift
                g = Grade.objects.get(pk=grade)
                c.grade=g
                s= School.objects.get(pk=school)
                c.school=s
                c.save()             
                type = "success"
              
    except: 
        
        print 'Se ha producido  un error'
        message = "erorr"
        
    result = simplejson.dumps({            
                 "message":message,
                 "type":type,
             }, cls = LazyEncoder)
    return HttpResponse(result, mimetype = 'application/javascript')
         


@login_required(login_url='/login/')
def classroom_save_edit(request):
    message = ""
    type = "error"
    print('entre al save edit')
    try:

        if request.POST:
            print('entre al post')
            country =request.POST['select_country']           
            department = request.POST['select_department']    
            school= request.POST['select_school']
            grade= request.POST['select_grade'] 
            className=request.POST['class_name']      
            shift=request.POST['select_shift']
            code=request.POST['code_class'] 
            c = ClassRoom.objects.get(pk=code)
            c.class_letter = className
            c.shift = shift
            g = Grade.objects.get(pk=grade)
            c.grade=g
            s= School.objects.get(pk=school)
            c.school=s
            c.save()
            
            type = "success"
    except: 
        print('entre a la execpcion')
        message = "No hay alumnos"

    result = simplejson.dumps({            
            "message":message,
            "type":type,
        }, cls = LazyEncoder)
    return HttpResponse(result, mimetype = 'application/javascript')	

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def load_departments(request):

    dictionary_departments = {}
    
    message = ""
    type = "error"
    try:
        if request.POST:
                     
            id_country =request.POST['id_country']
            
            c = Country.objects.get(pk=id_country)
            
            departments = Department.objects.filter(country=c)  
              
            
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

@login_required(login_url='/login/')
def load_schools(request):

    dictionary_schools = {}
    
    message = ""
    type = "error"
    try:
        if request.POST:
                     
            id_department =request.POST['id_department']
            
            d = Department.objects.get(pk=id_department)
            
            schools = School.objects.filter(department=d)  
              
            
            type = "success"

            for s in schools:                
                dictionary_schools[s.id] = {
                    
                    "name": s.name,
                    "id": s.id                               
                }

        result = simplejson.dumps({
        "dictionary_schools":dictionary_schools,
        "message":message,
        "type":type,
        }, cls = LazyEncoder)
        return HttpResponse(result, mimetype = 'application/javascript')
            #return render_to_response('classroomList.html',{'countrys':countrys, 'departments': departments, 'schools': schools,'grades': grades}, context_instance = RequestContext(request))
    except School.DoesNotExist:
        message = "No hay escuelas"
    
    return HttpResponse(result, mimetype = 'application/javascript')

@login_required(login_url='/login/')
def load_classroom_code(request):
    message = ""
    type = "error"
    dictionary_classroom={}
    
    try:
        if request.POST:
            code_classroom =request.POST['code_class_to_delete']
            c = ClassRoom.objects.get(pk=code_classroom)
            dictionary_classroom[c.code] = {
                       
                    "code":c.code,
                    }

        type = "success"
        result = simplejson.dumps({
        "dictionary_classroom":dictionary_classroom,    
        "message":message,
        "type":type,
        }, cls = LazyEncoder)
        return HttpResponse(result, mimetype = 'application/javascript')
    except ClassRoom.DoesNotExist:
        message = "No hay aula"    
    return HttpResponse(result, mimetype = 'application/javascript')


@login_required(login_url='/login/')
def classroom_delete(request):

    message = ""
    type = "error"

    try:
        if request.POST:
           
            code =request.POST['code_class_to_delete']

            c = ClassRoom.objects.get(pk=code)
            c.delete()
           # print('borro aula', co)

        type = "success"

        result = simplejson.dumps({   
        "message":message,
        "type":type,
        }, cls = LazyEncoder)
        return HttpResponse(result, mimetype = 'application/javascript')
    except ClassRoom.DoesNotExist:
        message = "No hay aula"    
    return HttpResponse(result, mimetype = 'application/javascript')



def generate_classroom_code():
    code = ''
    chars=string.ascii_uppercase + string.digits
    size=5
    existe = True 
    while existe:        
        code = ''.join(random.choice(chars) for _ in range(size))
        try:
            classroom = ClassRoom.objects.get(pk=code)
            print 'NO EXISTE CODIGO'
        except:
            print 'EXISTE CODIGO'
            existe = False    
    return code
	
