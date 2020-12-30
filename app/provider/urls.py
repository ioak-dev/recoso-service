from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('<str:project_reference>/domain/<str:domain_name>', views.get_domain),
    path('<str:project_reference>/domain/<str:domain_name>/<str:id>', views.get_domain_by_id),

    re_path(r'^(?P<project_reference>[\w]+)/domain/(?P<domain_name>[\w]+)/(?P<custom_path>.+)', views.get_domain_custom_path),

    # re_path(r'^(?P<project_reference>[\w]+)/domain/(?P<domain_name>[\w]+)/_/(?P<custom_path>.+)', views.get_domain_custom_path),
    # re_path(r'^(?P<project_reference>[\w]+)/domain/(?P<domain_name>[\w]+)/(?P<id>[a-zA-Z0-9._*-]+)/_/(?P<custom_path>.+)', views.get_domain_by_id_custom_path),
    
    
    path('<str:project_reference>/custom/<str:endpoint_name>', views.actions_for_custom_endpoint)
]