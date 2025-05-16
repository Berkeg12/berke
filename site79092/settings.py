from pathlib import Path

# Proje dizin yolu
BASE_DIR = Path(__file__).resolve().parent.parent

# Güvenlik ayarları
SECRET_KEY = 'django-insecure-#-e8zb%7pa3fxxpcw*0g&$b2i9byr5vm#7(k1m@mf^gb!)^hn5'
DEBUG = True
ALLOWED_HOSTS = []

# Yüklü uygulamalar
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Ana uygulama
]

# Ara katmanlar
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'site79092.urls'

# Şablon (template) ayarları
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Özel template klasörü belirtilecekse buraya ekle
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'site79092.wsgi.application'

# Veritabanı ayarları (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Şifre doğrulama kuralları
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Uluslararası ayarlar
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Statik dosyalar (CSS, JS, img)
STATIC_URL = 'static/'

# Medya dosyaları (kullanıcı yüklemeleri, avatar vs.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Varsayılan birincil anahtar türü
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Kimlik doğrulama yönlendirmeleri
LOGIN_REDIRECT_URL = '/'      # Giriş sonrası yönlendirilecek sayfa
LOGIN_URL = 'login'           # Giriş yapılmadan erişimde yönlenecek sayfa

# E-posta gönderimi (şifre sıfırlama işlemleri için)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Geliştirme ortamı için
DEFAULT_FROM_EMAIL = 'noreply@example.com'


