from django.urls import path, re_path

from . import views


urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('forecast/', views.forecast, name="forecast"),
]

