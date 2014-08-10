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
                login(request, user)
                return HttpResponseRedirect('/aulas/lista/')
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
    return render_to_response('logout.html' , context_instance=RequestContext(request))

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
        try:
            dob = datetime.datetime.strptime(str_dob,"%d/%m/%Y").date()
        except:
            dob = datetime.datetime.now().date()

        try:
            t = Teacher.objects.get(username=username)
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

def register_success(request):
    try:
        username = request.user.username
    except:
        username = ""
    return render_to_response('register_success.html', {'username':username}, context_instance=RequestContext(request))