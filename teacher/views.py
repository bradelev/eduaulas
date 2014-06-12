
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
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/panel/lista/')
    return render_to_response('login.html', context_instance=RequestContext(request))
 
@login_required(login_url='/login/')
def inicio(request):
    return render_to_response('index.html' , context_instance=RequestContext(request))

def register(request):
    return render_to_response('register.html', context_instance=RequestContext(request))