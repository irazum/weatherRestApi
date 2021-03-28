from django.urls import path, re_path
from . import views


urlpatterns = [
    path('weather', views.weather, name='weather'),
    path('forecast', views.forecast, name="forecast"),
    re_path(r"(?P<url>.*)", views.rest_urls, name="rest_urls")
]
