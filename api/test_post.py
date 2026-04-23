from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class PostTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='test',
            password='123456'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        data = {
            "title": "Test",
            "content": "This is valid content"
        }

        response = self.client.post('/api/posts/', data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], "Test")

    def test_invalid_post(self):
        data = {
            "title": "",
            "content": "short"
        }

        response = self.client.post('/api/posts/', data)

        self.assertEqual(response.status_code, 400)

    def test_permission(self):
        other = User.objects.create_user(
            username='other',
            password='123456'
        )

        post = self.client.post('/api/posts/', {
            "title": "Test",
            "content": "Valid content here"
        }).data

        self.client.force_authenticate(user=other)

        response = self.client.put(f"/api/posts/{post['id']}/", {
            "title": "Hack",
            "content": "Hack content"
        })

        self.assertEqual(response.status_code, 403)