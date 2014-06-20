# encoding: utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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
from datetime import date


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
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        msg = ""
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/panel/lista/')
        else:
            msg = "No existe este usuario o la contraseña es incorrecta"
    return render_to_response('login.html', context_instance=RequestContext(request))
 
@login_required(login_url='/login/')
def inicio(request):
    return render_to_response('index.html' , context_instance=RequestContext(request))

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
        #dob = request.POST['dateofbirth']
        dob = date(1985,11,11)

        try:
            t = Teacher.objects.get(email=email)
            msg = "Ya existe un usuario con este correo"
        except Teacher.DoesNotExist:
            t = Teacher(
                name=first_name, 
                last_name=last_name, 
                date_of_birth=dob, 
                gender=gender, 
                email=email, 
                nickname=username, 
                password=password)
            t.save()
            msg = "Gracias por tu registrp"
            registered = True
    print "%s - %s " % (registered, msg)
        
    return render_to_response('register.html', {'registered': registered, 'msg':msg}, context_instance=RequestContext(request))