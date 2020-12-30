from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('jwttest', views.jwtTest),
    path('signin/jwt', views.signin_jwt),
    path('session/<str:auth_key>', views.get_session),
    path('session/appspace/<str:auth_key>', views.get_session_appspace)
]
