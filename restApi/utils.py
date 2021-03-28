from .personal_data import openWeather_token


def temp_convert(num, scale):
    """
    конвертирует переданную температуру
    из кельвинов в цельсии или фаренгейты
    """
    pass


def basicParams_handler(request):
    city = request.GET.get('city')
    scale = request.GET.get('scale')
    scale = scale if scale == 'imperial' else "metric"
    params = {'q': city, 'appid': openWeather_token, 'units': scale}
    return params
