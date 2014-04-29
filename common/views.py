from django.shortcuts import render, render_to_response
from django.template import RequestContext
import meta.models

def index(request):
    # TODO Add docstring here
    # TODO Make wrapper for RequestContext
    # TODO Clean up view code here
    token_required = False
    token_object = meta.models.Data.objects.get(tag='new-users')

    if token_object.setting == 0 and token_object.data == 'token':
        token_required = True

    data = {'token_required': token_required}

    return render_to_response('index.html', data,
                              context_instance=RequestContext(request))