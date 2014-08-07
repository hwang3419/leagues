from django.http import HttpResponse 
from django.shortcuts import render_to_response
from django.template import RequestContext
def match(request):
    return render_to_response('match.html', context_instance = RequestContext(request))

def summary(request):
    return render_to_response('summary.html', context_instance = RequestContext(request))

def comment(request):
    return render_to_response('comment.html', context_instance = RequestContext(request))

def trend(request):
    return render_to_response('trend.html', context_instance = RequestContext(request))