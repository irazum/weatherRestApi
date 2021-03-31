from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page

import requests
import logging

from .utils import basicParams_handler


api_commonUrl = "https://api.openweathermap.org/data/2.5/"
problem_message_data = {"cod": 404, "message": "internal server error, please try again later"}

# log conf
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s!%(levelname)s: %(message)s')
views_log = logging.getLogger("views_log")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def weather(request):
    """Current weather
    :param request: HttpRequest
    :return: JSON
    """
    url = f"{api_commonUrl}weather/"
    params = basicParams_handler(request)

    try:
        r = requests.get(url, params=params)
    except requests.exceptions.RequestException as err:
        views_log.error(f"weather: {err}")
        return Response(problem_message_data, status=404)
    # auth problem handler
    if r.status_code == 401 or r.status_code == 429:
        views_log.error(f"weather: status_code 401, data: {r.json()}")
        return Response(problem_message_data, status=404)

    return Response(r.json())


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def forecast(request):
    """5 day weather forecast for each 3 hours
    :param request: HttpRequest
    :return: JSON
    """
    url = f"{api_commonUrl}forecast/"
    params = basicParams_handler(request)
    if request.GET.get('cnt'):
        params['cnt'] = request.GET.get('cnt')

    try:
        r = requests.get(url, params=params)
    except requests.exceptions.RequestException as err:
        views_log.error(f"forecast: {err}")
        return Response(problem_message_data, status=404)
    # auth problem handler
    if r.status_code == 401 or r.status_code == 429:
        views_log.error(f"forecast: status_code 401, data: {r.json()}")
        return Response(problem_message_data, status=404)

    return Response(r.json())
