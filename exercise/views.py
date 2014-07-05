from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from classroom.models import  ClassRoom, Grade
from exercise.models import Exercise, Lectures, Subject, Unit
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

def contents(request, grade, subject, unit):
	error = False
	try:
		s = Subject.objects.get(name=subject)
		g = Grade.objects.get(name=grade)
		u = Unit.objects.get(letter=unit, grade=g, subject=s)
		experiments = Lectures.objects.filter(lecture_type='EXPERIMENT')
		lectures = Lectures.objects.filter(lecture_type='LECTURE')
		exercises = Exercise.objects.filter(unit=u, grade=g, unit__subject=s)
		homeworks = Lectures.objects.filter(lecture_type='HOMEWORK')
	except:
		error = True

	return render_to_response('contents.html',{'subject':s, 'unit':u, 'experiments':experiments,'lectures':lectures, 'exercises':exercises, 'homeworks':homeworks, 'error':error}, context_instance = RequestContext(request))