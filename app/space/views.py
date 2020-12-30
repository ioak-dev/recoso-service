from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
from app.space.service import do_create, do_get_space, do_get_banner, do_update_space
import json, base64

@api_view(['POST'])
def create(request):
    response = do_create({
        'name': request.POST.get('spaceName'),
        'ownerEmail': request.POST.get('email')
    })
    return JsonResponse(response[1], status=response[0])

@api_view(['GET'])
def get_banner(request, space_id):
    response = do_get_banner(space_id)
    return HttpResponse(response[1], status=response[0])

@api_view(['GET'])
def get_space(request, space_id):
    response = do_get_space(space_id)
    return JsonResponse(response[1], status=response[0])

@api_view(['PUT'])
def add_stage(request, space_id):
    response = do_update_space(space_id, request.body)
    return JsonResponse(response[1], status=response[0])