from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.request import Request
from unittest import mock


# Create your tests here.
class NetworkCaseTest(APITestCase):
    def setUp(self):
        self.test_data1 = {'main': 'some_data'}

    @mock.patch('restApi.views.basicParams_handler')
    @mock.patch("restApi.views.requests")
    def test_weather(self, mock_requests, mock_bpHandler):
        # set return values of used mock attributes
        mock_requests.get.return_value = mock_requests.response
        mock_requests.response.json.return_value = self.test_data1
        mock_bpHandler.return_value = {}

        # call views.weather
        url = reverse('weather')
        response = self.client.get(url, params={}, format='json')

        # check that the views.weather calls mock_bpHandler with Request instance obj
        self.assertTrue(isinstance(mock_bpHandler.call_args.args[0], Request))
        # check mock_requests.get was called by the api_url first parameter
        api_url = "https://api.openweathermap.org/data/2.5/weather"
        self.assertEqual(mock_requests.get.call_args.args[0], api_url)
        # check that the views.weather calls mock_requests.response.json and sends returned data
        self.assertEqual(response.data, self.test_data1)

    @mock.patch('restApi.views.basicParams_handler')
    @mock.patch("restApi.views.requests")
    def test_forecast(self, mock_requests, mock_bpHandler):
        mock_requests.get.return_value = mock_requests.response
        mock_requests.response.json.return_value = self.test_data1
        mock_bpHandler.return_value = {}

        # call views.forecast
        url = reverse('forecast')
        response = self.client.get(url, params={}, format='json')

        # check that the views.weather calls mock_bpHandler with Request instance obj
        self.assertTrue(isinstance(mock_bpHandler.call_args.args[0], Request))
        # check mock_requests.get was called by the api_url first parameter
        api_url = "https://api.openweathermap.org/data/2.5/forecast"
        self.assertEqual(mock_requests.get.call_args.args[0], api_url)
        # check that the views.weather calls mock_requests.response.json and sends returned data
        self.assertEqual(response.data, self.test_data1)

    def test_restUrls_1(self):
        response = self.client.get('/api/someurl')
        self.assertEqual(response.data, {"cod": "404", "message": "Internal error"})

