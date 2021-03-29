from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('forecast/', views.forecast, name="forecast"),
]

