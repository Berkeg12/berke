import os
from celery import Celery

# Django ayarlarını belirt
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site79092.settings')

app = Celery('site79092')

# Celery ayarlarını Django settings.py'den al
app.config_from_object('django.conf:settings', namespace='CELERY')

# Tüm Django app'lerinde tasks.py dosyasını otomatik bul
app.autodiscover_tasks()
