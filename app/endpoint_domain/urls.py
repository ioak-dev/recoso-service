from django.urls import path

from . import views

urlpatterns = [
    path('<str:project_id>', views.get_endpoint_domain),
    path('', views.update_endpoint_domain),
    path('<str:id>', views.delete_endpoint_domain)
]
