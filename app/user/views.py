from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
import app.user.service as service

@api_view(['GET', 'PUT'])
def do(request, space_id):
    if request.method == 'GET':
        response = service.find(request, space_id)
        return JsonResponse(response[1], status=response[0])
    elif request.method == 'PUT':
        response = service.do_update_user(request, space_id)
        return JsonResponse(response[1], status=response[0])

@api_view(['GET'])
def get_all(request, space_id):
    if request.method == 'GET':
        response = service.find_all(request, space_id)
        return JsonResponse(response[1], status=response[0])

@api_view(['GET'])
def permittedActions(request, space_id):
    response = service.find_permitted_actions(space_id, request.user_id)
    return (200, {'data': response})
