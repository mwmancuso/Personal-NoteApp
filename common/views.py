from django.shortcuts import render, render_to_response
import meta.models

def index(request):
    token_required = False
    token_object = meta.models.Data.objects.get(tag='new-users')

    if token_object.setting == 0 and token_object.data == 'token':
        token_required = True

    return render_to_response('index.html', {'token_required': token_required})