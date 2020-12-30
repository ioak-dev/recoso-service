from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
import app.provider.service as service

@api_view(['GET'])
def get_domain(request, space_id, project_reference, domain_name):
    if request.method == 'GET':
        response = service.get_domain(request, space_id, project_reference, domain_name)
        return JsonResponse(response[1], status=response[0], safe=False)

@api_view(['GET'])
def get_domain_custom_path(request, space_id, project_reference, domain_name, custom_path):
    print(project_reference, domain_name, custom_path)
    if request.method == 'GET':
        response = service.get_domain(request, space_id, project_reference, domain_name)
        return JsonResponse(response[1], status=response[0], safe=False)

@api_view(['GET'])
def get_domain_by_id(request, space_id, project_reference, domain_name, id):
    if request.method == 'GET':
        response = service.get_domain_by_id(request, space_id, project_reference, domain_name, id)
        return JsonResponse(response[1], status=response[0])

@api_view(['GET'])
def get_domain_by_id_custom_path(request, space_id, project_reference, domain_name, id, custom_path):
    if request.method == 'GET':
        response = service.get_domain_by_id(request, space_id, project_reference, domain_name, id)
        return JsonResponse(response[1], status=response[0])

@api_view(['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
def actions_for_custom_endpoint(request, space_id, project_reference, endpoint_name):
    response = service.actions_for_custom_endpoint(request, space_id, project_reference, endpoint_name, request.method)
    return JsonResponse(response[1], status=response[0], safe=False)
