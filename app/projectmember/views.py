from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
import app.projectmember.service as service

@api_view(['GET'])
def get(request, space_id, project_id):
    if request.method == 'GET':
        response = service.find(request, space_id, project_id)
        return JsonResponse(response[1], status=response[0])
    
@api_view(['DELETE'])
def delete(request, space_id, id):
    if request.method == 'DELETE':
        response = service.delete(request, space_id, id)
        return JsonResponse(response[1], status=response[0])

@api_view(['POST'])
def add(request, space_id):
    if request.method == 'POST':
        response = service.add(request, space_id, request.body)
        return JsonResponse(response[1], status=response[0])