# encoding: utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

from django.utils import simplejson
from django.http import *
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.views.decorators.csrf import ensure_csrf_cookie
#from django.core.context_processors import csrf
from teacher.models import Teacher
from configurations.models import Configuration
import datetime
import json


class LazyEncoder(simplejson.JSONEncoder):
    """Encodes django's lazy i18n strings.
    """
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return obj

def login_user(request):
    logout(request)
    username = password = ''
    msg = ""
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                try:
                    teacher = Teacher.objects.get(user=user)
                    login(request, user)
                    return HttpResponseRedirect('/aulas/lista/')
                except:
                    msg = "Usuario debe ser un Docente"
        else:
            msg = "No existe este usuario o la contraseña es incorrecta"
    else:
        msg = ""
    return render_to_response('login.html',{'msg':msg}, context_instance=RequestContext(request))
 
@login_required(login_url='/login/')
def inicio(request):
    return render_to_response('index.html' , context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")
    

def register(request):
    registered = False
    msg = ""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        gender = request.POST['gender']
        str_dob = request.POST['dateofbirth']

        print str_dob, 'fecha nac'
        try:
            dob = datetime.datetime.strptime(str_dob,"%d/%m/%Y").date()
            print 'converti exitosamente'
        except:
            dob = datetime.datetime.now().date()
            print 'NOOO converti exitosamente'

        try:
            t = Teacher.objects.get(user__username=username)
            msg = "Ya existe un usuario con este usuario"
        except:
            user = User.objects.create_user(username,email,password)
            user.is_staff = False
            user.is_active = True
            user.save()
            
            t = Teacher(
                name=first_name, 
                last_name=last_name, 
                date_of_birth=dob, 
                gender=gender, 
                user=user)
            t.save()
            c = Configuration(teacher=t)
            c.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            msg = "Gracias por tu registro"
            registered = True
            return HttpResponseRedirect("/registro_exitoso/")
        
    return render_to_response('register.html', {'registered': registered, 'msg':msg}, context_instance=RequestContext(request))

def user_validation(request):
    exist_user = False
    print "entra"
    type = "error"
    try:
        if request.POST:
            user_post = request.POST['user']
            try:
                print "entra"
                #user = User.objects.get(username=user_post)
                exist_user = True
            except:
                pass
            type = "success"
    except:
        message = "Hubo un error"
    result = simplejson.dumps({
                "exist_user":exist_user,
                "message":message,
                "type":type,
                }, cls = LazyEncoder)
    return HttpResponse(result, mimetype = 'application/javascript')

def register_success(request):
    try:
        username = request.user.username
        return HttpResponseRedirect("/aulas/lista/")
    except:
        username = ""
    return render_to_response('register_success.html', {'username':username}, context_instance=RequestContext(request))

