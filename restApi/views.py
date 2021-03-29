from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import requests

from .utils import basicParams_handler


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def weather(request):
    """Current weather
    :param request: HttpRequest
    :return: JSON
    """
    url = "https://api.openweathermap.org/data/2.5/weather/"
    params = basicParams_handler(request)
    r = requests.get(url, params=params)

    return Response(r.json())


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def forecast(request):
    """5 day weather forecast for each 3 hours
    :param request: HttpRequest
    :return: JSON
    """
    url = "https://api.openweathermap.org/data/2.5/forecast/"
    params = basicParams_handler(request)
    if request.GET.get('cnt'):
        params['cnt'] = request.GET.get('cnt')
    r = requests.get(url, params=params)

    return Response(r.json())
