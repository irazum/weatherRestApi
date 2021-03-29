from rest_framework.test import APITestCase
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

    def test_getToken(self):
        data = {
            "username": self.user.username,
            "password": self.password
        }
        response = self.client.post('/get-token/', data=data, format='json')
        self.assertEqual(response.data.get('token'), self.token)


    def test_register(self):
        """
        Добавить тестирование, что при корректных данных запроса нам возвращается токен
        .., при некорректных данных status запроса
        """
        pass
