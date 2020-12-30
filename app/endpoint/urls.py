from django.urls import path

from . import views

urlpatterns = [
    path('<str:project_id>', views.get_endpoint),
    path('', views.update_endpoint),
    path('<str:id>', views.delete_endpoint)
]
