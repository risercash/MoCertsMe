import os
from MoCerts.log_settings import log_settings
from secret.config import *
from django.urls import reverse_lazy

try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHATID = os.getenv("CHATID")
SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = os.getenv("SOCIAL_AUTH_TELEGRAM_BOT_TOKEN")


MONEY_ADMIN = {'username': 'money', 'first_name': 'MONEY_ADMIN', 'last_name': 'money',
               'email': 'mocerts.com@gmail.com', 'password': os.getenv("MONEY_ADMIN_PASSWORD")}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'MainApp',
    'Bot',

    'easy_thumbnails',
    'modeltranslation',
    'ckeditor',
    'ckeditor_uploader',
    # 'djcelery_email',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    # 'social_django',
    # 'allauth.socialaccount.providers.instagram',
]


ROOT_URLCONF = 'MoCerts.urls'

WSGI_APPLICATION = 'MoCerts.wsgi.application'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'middleware.filter_ip_middleware.FilterIPMiddleware'
]

ROOT_URLCONF = 'MoCerts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Templates', BASE_DIR / 'Templates' / 'allauth', ],
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_DIR = os.path.join(BASE_DIR, 'media/')
MEDIA_ROOT = MEDIA_DIR

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
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1


AUTH_USER_MODEL = 'MainApp.CustomUser'
ACCOUNT_ADAPTER = 'MainApp.adapter.MyAccountAdapter'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {'signup': 'MainApp.forms.MySignupForm',
                 'login': 'MainApp.forms.MyLoginForm'}
SOCIALACCOUNT_PROVIDERS = \
    {
        'facebook':
        {'METHOD': 'oauth2',
         'SCOPE': ['email', 'public_profile', 'user_friends'],
         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
         'FIELDS': [
             'id',
             'email',
             'name',
             'first_name',
             'last_name',
             'verified',
             'locale',
             'timezone',
             'link',
             'gender',
             'updated_time'],
         'EXCHANGE_TOKEN': True,
         'LOCALE_FUNC': lambda request: 'kr_KR',
         'VERIFIED_EMAIL': False,
         'VERSION': 'v2.4'}
    }


# Настройки почтового сервера
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 25
EMAIL_USE_TLS = False

SERVER_EMAIL = EMAIL_HOST_USER
# Используется для отправки email после регистрации
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# Почта админа для получения уведомлении
NOTIFICATION_EMAIL = 'risercash@gmail.com'
ADMINS = os.getenv("ADMINS")
POSTADMIN = os.getenv("POSTADMIN")
EMAIL_SUBJECT_PREFIX = '[MoCerts] '

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

LOGIN_REDIRECT_URL = reverse_lazy('create_certificate')

# Логирование
LOGGING = log_settings

# Настройки ckeditor
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_IMAGE_MAX_WIDTH = 200
CKEDITOR_CONFIGS = {
    'default': {
        'width': 1200,
        'height': 1000,
        'toolbar': 'Custom',
        'extraPlugins': ','.join([
            'codesnippet',
            'youtube', 
        ]),
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike',
             'Subscript', 'Superscript', '-', 'RemoveFormat',],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'sourcearea', 'SpecialChar'],
            ['Link', 'Unlink', 'Anchor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language'],
            ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText',
                'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
            ['Maximize', 'ShowBlocks',]
        ],

    },

}
