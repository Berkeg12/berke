from celery import shared_task
from .models import Post

@shared_task
def send_post_notification(post_id):
    post = Post.objects.get(pk=post_id)
    print(f"Post Gönderimi Başarılı: {post.title}")
    
