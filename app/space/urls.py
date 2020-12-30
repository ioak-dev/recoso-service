from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('create', views.create),
    path('<str:space_id>', views.get_space),
    path('banner/<str:space_id>', views.get_banner),
    path('stage/<str:space_id>', views.add_stage)
]