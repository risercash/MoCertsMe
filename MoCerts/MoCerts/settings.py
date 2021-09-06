import os
from MoCerts.log_settings import log_settings
from secret.config import *
from .prod_settings import *


MONEY_ADMIN = {'username':'money', 'first_name':'MONEY_ADMIN', 'last_name':'money',
                'email':'mocerts.com@gmail.com', 'password':'Ya552026'}



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    
    'MainApp',

    'django_telegram_login',

    'easy_thumbnails',
    'modeltranslation',
    'embed_video',
    'ckeditor',
    'ckeditor_uploader',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.telegram',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'middleware.filter_ip_middleware.FilterIPMiddleware'
]

ROOT_URLCONF = 'MoCerts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Templates', BASE_DIR / 'Templates' / 'allauth',],
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

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

WSGI_APPLICATION = 'MoCerts.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_L10N = True

USE_TZ = True
#static

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'static'),
]
STATIC_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_URL = '/static/'

#MEDIA_URL = '/media/'
#MEDIA_DIR = os.path.join(BASE_DIR, 'media/')
#MEDIA_ROOT = MEDIA_DIR


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

THUMBNAIL_ALIASES = {
    '':
        {
            'my_certs_page': {'size': (182, 129), 'crop': 'smart'},
            'select_certs_page': {'size': (210, 150), 'crop': 'smart'}
        }
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = '1978440363:AAF-FOftfttv5MmM6VrIRDPOfSS75Bf7NqI'

SITE_ID = 1


AUTH_USER_MODEL = 'MainApp.CustomUser'
ACCOUNT_ADAPTER = 'MainApp.adapter.MyAccountAdapter'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {'signup': 'MainApp.forms.MySignupForm', 'login': 'MainApp.forms.MyLoginForm'}
# Настройки почтового сервера
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'


# адрес сервера почты для всех один и тот же
# порт smtp сервера тоже одинаковый

# пароль от почты
EMAIL_USE_TLS = True
# Написать email администратора, для отправки сообщении при ошибках
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Используется для отправки email после регистрации
EMAIL_SUBJECT_PREFIX = '[MoCerts] '

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


SOCIALACCOUNT_PROVIDERS = {
    'telegram': {
        'TOKEN': '1978440363:AAF-FOftfttv5MmM6VrIRDPOfSS75Bf7NqI'
    }
}

# Логирование
LOGGING = log_settings

# Настройки ckeditor
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_IMAGE_MAX_WIDTH = 200
CKEDITOR_CONFIGS={
  'default': {
    'width': '100%',
    'height': 400,
    'toolbar': 'Custom',
    'extraPlugins': ','.join([
      'codesnippet',
      'youtube'
    ]),
    'toolbar_Custom': [
      [
        'Bold',
        'Italic',
        'Underline'
      ],
      [
        'Font',
        'FontSize',
        'TextColor',
        'BGColor'
      ],
      [
        'NumberedList',
        'BulletedList',
        '-',
        'Outdent',
        'Indent',
        '-',
        'JustifyLeft',
        'JustifyCenter',
        'JustifyRight',
        'JustifyBlock'
      ],
      [
        'Link',
        'Unlink'
      ],
      [
        'Image',
        'Youtube',
        'RemoveFormat',
        'CodeSnippet',
        'Source',
      ]
    ],
    
  },
  
}
