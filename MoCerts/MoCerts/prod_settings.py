import os
from pathlib import Path
from secret.config import *

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

ALLOWED_HOSTS = ['mocerts.com', 'localhost', '127.0.0.1', '*']

#Настройки для базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('MySQL_DB'),
#         'USER': os.environ.get('NAME_USER_DB'),
#         'PASSWORD': os.environ.get('PASSWORD_DB'),
#         'HOST': os.environ.get('HOST_DB'),
#         'PORT': os.environ.get('PORT_DB'),
#     }
# }


#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = '/static/'
