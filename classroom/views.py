from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
import random
import string
from classroom.models import  ClassRoom, Grade
from location.models import School, Country, Department
import datetime
from django.utils import simplejson
from django.http import *
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.views.decorators.csrf import ensure_csrf_cookie
from configurations.models import Configuration
from teacher.models import Teacher
#from django.http import Http500
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
import socket

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
    
    return render_to_response('classroom_list.html', context_instance = RequestContext(request))



@login_required(login_url='/login/')
def load_teacher_configuration(request):
    message =""
    type = "error"
    
    corrects_points = ''
    incorrect_points = ''
    quantity_exercises = ''
    time_to_update_panel = ''
    try:
        userid = request.user.id
        teacher = Teacher.objects.get(user=userid)
        teacher_config = Configuration.objects.get(teacher=teacher.id)
        
        try:
            teacher_config = Configuration.objects.get(teacher=teacher.id)
            corrects_points = teacher_config.correct_points
            incorrect_points = teacher_config.incorrect_points
            quantity_exercises = teacher_config.minimum_quantity_exercise
            time_to_update_panel = teacher_config.time_to_update_panel
       
            type = "success"
        except:
            message = "No se pudo obtener la configuracion"
            print message
        
    except:
        message="Debe loguearse como un maestro "
        return render_to_response('500.html',{"message":message}, context_instance = RequestContext(request))
    result = simplejson.dumps({
                        "corrects_points":corrects_points,
                        "incorrect_points": incorrect_points,
                        "quantity_exercises": quantity_exercises,
                        "time_to_update_panel": time_to_update_panel,
                        "message":message,
                        "type":type,
                }, cls = LazyEncoder)
    return HttpResponse(result, mimetype = 'application/javascript')


@login_required(login_url='/login/')
def update_teacher_configuration(request):    
    print 'actualizando configuracion'
    corrects_points = ''
    incorrect_points = ''
    quantity_exercises = ''
    time_to_update_panel =''
    message=''
    type='error'
    msg =''
    try:
        if request.POST:
            print 'unooo'
            correct_points =request.POST['correct_points']  
            incorrect_points = request.POST['incorrect_points']          
            quantity_exercises = request.POST['quantity_exercises']       
            time_to_update_panel = request.POST['time_to_update_panel']
            print 'dos'
            try:
                if (correct_points != '' and incorrect_points != '' and quantity_exercises != '' and time_to_update_panel != ''):
                    
                    userid = request.user.id
                    user_name = request.user.username
                    teach = Teacher.objects.get(user=userid)
                    teacher_config = Configuration.objects.get(teacher=teach)
                    print correct_points ,'correctos', incorrect_points, 'incorrectos', quantity_exercises, 'cantidad',time_to_update_panel,'tiempo'
                    teacher_config.correct_points = correct_points
                    teacher_config.incorrect_points = incorrect_points
                    teacher_config.minimum_quantity_exercise = quantity_exercises
                    teacher_config.time_to_update_panel = time_to_update_panel
                   
                    teacher_config.save()

                  
                    type='success'
                else:
                    msg = 'No puede haber campos vacios' 
            except:
                message = "Hubo un error al guardar"
                print message

    except:
        message = "Hubo un error"
        print message
    print type    
    result = simplejson.dumps({
                   
                    "message":message,
                    "type":type,
            }, cls = LazyEncoder)
    return HttpResponse(result, mimetype = 'application/javascript')


@login_required(login_url='/login/')
def load_teacher(request):
    message =""
    type = "error"
    
    try:
        userid = request.user.id
        teacher = Teacher.objects.get(user=userid)
        teacher_config = Configuration.objects.get(teacher=teacher.id)
        
        user = request.user.username
        name = teacher.name
        last_name = teacher.last_name
        email = teacher.user.email
        gender = teacher.gender
        password = teacher.user.password
        date_birth = str(teacher.date_of_birth)
       
        type = "success"
        
    except:
        message="Debe loguearse como un maestro "
        return render_to_response('500.html',{"message":message}, context_instance = RequestContext(request))
    result = simplejson.dumps({
                        "name":name,
                        "user": user,
                        "last_name": last_name,
                        "email": email,
                        "gender": gender,
                        "date_birth":date_birth,
                        "password":password,
                        "message":message,
                        "type":type,
                }, cls = LazyEncoder)
    return HttpResponse(result, mimetype = 'application/javascript')



@login_required(login_url='/login/')
def update_teacher_info(request):    
    print 'updaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    message='iniciali'
    type = "error"
    msg =''
    teach = None
    context = {}
    try:
        if request.POST:
            
            name =request.POST['name']  
            last_name = request.POST['last_name']          
            email = request.POST['email']       
            user = request.POST['user']
            gender = request.POST['gender']
            date_birth = request.POST['date_birth']
            password = request.POST['password']
            
            try:
                dob = datetime.datetime.strptime(date_birth,"%Y-%m-%d").date()
                print 'Fecha convertida exitosamente'
            except:
                dob = datetime.datetime.now().date()
                print 'Error al convertir la fecha'
                return HttpResponse(simplejson.dumps(result), mimetype = 'application/json')
            try:
                if (name != '' and last_name != '' and email != ''):
                    
                    userid = request.user.id
                    user_name = request.user.username
                    teach = Teacher.objects.get(user=userid)
                    teach.name = name                                           
                    teach.last_name = last_name
                    user = User.objects.get(pk=userid)
                    if password != '':
                        print password
                        user.password = password
                    #user.email = email
                    user.save() 
                    teach.date_of_birth = dob
                    teach.gender = gender
                    teach.save()
                    type = "success"
                    
                else:
                    msg = 'No puede haber campos vacios' 
            except:
                message = "Hubo un error al guardar"
                print message  
                return HttpResponse(simplejson.dumps(result), mimetype = 'application/json') 
            
            
    except Teacher.DoesNotExist:
        message = "No existe maestro"
        print message
        return HttpResponse(simplejson.dumps(result), mimetype = 'application/json')

    except:
        message = "Hubo un error"
        print message
        return HttpResponse(simplejson.dumps(result), mimetype = 'application/json')
    print type    
    result = {"type":type }               
  
    return HttpResponse(simplejson.dumps(result), mimetype = 'application/json')


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
	
