from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class AuthTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        User.objects.create_user(
            username='test',
            password='123456'
        )

    def test_full_flow(self):
        # 1. Token olish
        res = self.client.post('/api/token/', {
            "username": "test",
            "password": "123456"
        })

        token = res.data['access']

        # 2. Token qo‘shish
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

        # 3. Post yaratish
        res = self.client.post('/api/posts/', {
            "title": "Integration",
            "content": "Integration content"
        })

        self.assertEqual(res.status_code, 201)

        # 4. Post olish
        res = self.client.get('/api/posts/')
        self.assertEqual(res.status_code, 200)