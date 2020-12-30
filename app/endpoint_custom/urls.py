from django.urls import path

from . import views

urlpatterns = [
    path('<str:project_id>', views.get_endpoint_custom),
    path('', views.update_endpoint_custom),
    path('<str:id>', views.delete_endpoint_custom)
]
