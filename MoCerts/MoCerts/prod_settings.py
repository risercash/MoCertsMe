import os
from pathlib import Path
from secret.config import *
from os import environ

HOST = '127.0.0.1'

BASE_DIR = Path(__file__).resolve().parent.parent

""" try:
    with open(os.path.join(BASE_DIR, 'secret/SECRET_KEY.txt'), 'r') as token:
        secret = token.read()
    SECRET_KEY = secret  # адрес сервера почты для всех один и тот же
except FileNotFoundError:
    print(Fore.RED + 'Не найден файл для SECRET_KEY')
    print(Style.RESET_ALL)
    SECRET_KEY = 'sefesfsefsefsfesff' """

DEBUG = True

ALLOWED_HOSTS = ['*']

# Настройки для базы данных 
DATABASES = {
    'default': {
        'ENGINE': environ.get('POSTGRES_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': environ.get('POSTGRES_DB', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': environ.get('POSTGRES_USER', 'user'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD', 'password'),
        'HOST': environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': environ.get('POSTGRES_PORT', '5432'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = environ.get('SOCIAL_AUTH_TELEGRAM_BOT_TOKEN')

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = '/static/'
