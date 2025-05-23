from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Post

class PostModelTest(TestCase):
    def test_create_post(self):
        user = User.objects.create_user(username='berke', password='12345')
        post = Post.objects.create(title='Test Başlık', content='Test İçerik', author=user)
        self.assertEqual(post.title, 'Test Başlık')
        self.assertEqual(str(post), 'Test Başlık')  # __str__ çıktısı
