from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import app.auth.service as service
from django.core import serializers
import json

@api_view(['GET'])
def jwtTest(request, space_id):
    response = service.do_jwttest(space_id)
    return HttpResponse(response[1], status=response[0])

@api_view(['POST'])
def signin_jwt(request, space_id):
    response = service.do_signin_via_jwt(space_id, request.body)
    return JsonResponse(response[1], status=response[0])

@api_view(['GET'])
def get_session(request, space_id, auth_key):
    response = service.get_session(space_id, auth_key, 'space')
    return JsonResponse(response[1], status=response[0])


@api_view(['GET'])
def get_session_appspace(request, space_id, auth_key):
    response = service.get_session(space_id, auth_key, 'appspace')
    return JsonResponse(response[1], status=response[0])
