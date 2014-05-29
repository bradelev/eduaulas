from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def lista(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def crear(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def compartir(request):
	render_to_response('index.html', context_instance = RequestContext(request))

def detalle(request, id):
	render_to_response('index.html', context_instance = RequestContext(request))	
