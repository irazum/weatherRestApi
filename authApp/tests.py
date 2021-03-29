from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User


class NetworkTestCase(APITestCase):
    def setUp(self):
        self.password = '1234'
        self.user = User.objects.create_user(
            username='test',
            password=self.password,
            email="test@email.com"
        )
        self.token = self.user.auth_token.key
        self.register_data = {
            "username": "test2",
            "email": "test2@email.com",
            "password": "1234"
        }
        self.register_url = reverse("register")

    def test_getToken(self):
        data = {
            "username": self.user.username,
            "password": self.password
        }
        response = self.client.post('/get-token/', data=data, format='json')
        self.assertEqual(response.data.get('token'), self.token)

    def test_register_token(self):
        """
        Добавить тестирование, что при корректных данных запроса нам возвращается токен
        .., при некорректных данных status запроса
        """
        response = self.client.post(self.register_url, self.register_data, format="json")
        self.assertTrue(response.status_code == 200 and response.data.get('token'))

    def test_register_notValid(self):
        self.register_data.pop('password')
        response = self.client.post(self.register_url, self.register_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_register_notValid2(self):
        self.client.post(self.register_url, self.register_data, format="json")
        response = self.client.post(self.register_url, self.register_data, format="json")
        self.assertEqual(response.status_code, 400)
