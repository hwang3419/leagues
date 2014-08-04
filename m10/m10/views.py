from django.http import HttpResponse 
from django.shortcuts import render_to_response
from django.template import RequestContext
def match(request):
    return render_to_response('match.html', context_instance = RequestContext(request))