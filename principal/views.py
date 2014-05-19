from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def panel(request):
	return render_to_response('index.html', context_instance = RequestContext(request))
