from rest_framework.test import APITestCase


class NetworkTestCase(APITestCase):
    def test_restUrls_1(self):
        response = self.client.get('/api/someurl')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {"cod": "404", "message": "Resource could not be found"})
