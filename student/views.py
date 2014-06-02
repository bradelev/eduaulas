from eduaulas import settings
from django.shortcuts import render
from students.models import Student
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.

def listarAlumnos(request):

	students = Student.objects.all()
	return render_to_response('index.html',{'students':students}, context_instance = RequestContext(request))