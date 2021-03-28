from rest_framework.test import APITestCase, APIRequestFactory

from restApi.utils import basicParams_handler
from restApi.personal_data import openWeather_token


class TestUtils(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_bpHandler(self):
        # create request obj
        params = {'city': 'Saint Petersburg', 'scale': 'imperial'}
        request = self.factory.get('/api/weather', params)

        check_params = {
            'q': params['city'],
            'appid': openWeather_token,
            'units': params['scale']
        }

        result = basicParams_handler(request)
        self.assertEqual(result, check_params)
