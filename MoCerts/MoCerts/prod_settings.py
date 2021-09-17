import os
from pathlib import Path


HOST = 'https://mocerts.com'

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY=os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['*', 'mocerts.com', 'localhost', '127.0.0.1']

# Настройки для базы данных 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Настройки для базы данных на Postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mocerts_new_db',
#         'USER': 'mocert',
#         'PASSWORD': 'mocert',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mocerts_new_db',
        'USER': 'mocerts_db',
        'PASSWORD': 'mocerts_db',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

# DROP DATABASE mocerts_db

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
