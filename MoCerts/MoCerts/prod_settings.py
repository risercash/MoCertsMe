import os
from pathlib import Path


HOST = 'https://mocerts.com'

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY=os.getenv("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ['*', 'mocerts.com', 'localhost', '127.0.0.1']

# Настройки для базы данных 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Настройки для базы данных на Postgresql
''''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ad_board_db',
        'USER': 'ad_board',
        'PASSWORD': 'ad_board',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}'''

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
