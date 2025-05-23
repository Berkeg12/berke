from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from core.models import Post
from rest_framework.authtoken.models import Token

print(">>> test_api.py aktif")

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apiberke', password='123456')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_post_create(self):
        print(">>> test_post_create çalıştı")
        data = {
            'title': 'API Test Post',
            'content': 'Bu bir API test içeriğidir.'
        }
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_list(self):
        print(">>> test_post_list çalıştı")
        Post.objects.create(title='Listelenen Post', content='İçerik', author=self.user)
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_unauthorized_access(self):
        print(">>> test_unauthorized_access çalıştı")
        self.client.credentials()  # Token'ı kaldır
        response = self.client.post('/api/posts/', {'title': 'Yetkisiz', 'content': 'Yasak'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

