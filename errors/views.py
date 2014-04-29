from django.http import HttpResponse
from django.shortcuts import render
import json
from errors import validators

def password_validator(request):
    # TODO Make docstring
    # TODO Clean up view here
    # TODO Make wrapper for JSON responses
    if request.method != 'POST':
        return HttpResponse(json.dumps({'error': 'Post required.'}),
                            content_type='application/json',
                            mimetype='application/json', status=404)

    try:
        validators.Password(request.POST.get('password', ''))
    except ValueError:
        return HttpResponse(json.dumps({'error': 'Invalid password.'}),
                            content_type='application/json',
                            mimetype='application/json', status=404)

    return HttpResponse(json.dumps({'message': 'OK'}),
                        content_type='application/json',
                        mimetype='application/json', status=200)