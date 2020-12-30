from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('project/<str:project_id>', views.get),
    path('', views.add),
    path('<str:id>', views.delete)
]