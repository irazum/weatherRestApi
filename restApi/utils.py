from .personal_data import openWeather_token


def basicParams_handler(request):
    city = request.GET.get('city')
    units = request.GET.get('units')
    units = units if units == 'imperial' else "metric"
    params = {'q': city, 'appid': openWeather_token, 'units': units}
    if request.GET.get('lang'):
        params['lang'] = request.GET.get('lang')
    return params
