"""
Django settings for gori project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import json
import os

DEBUG = True
# DEBUG = os.environ.get('MODE') == 'DEBUG'
# 실험이 되는지 확인하기위해  True생성
# STORAGE_S3 = True
# STORAGE_S3 = os.environ.get('STORAGE') == 'S3' or DEBUG is False
STORAGE_S3 = False
# STORAGE_S3 = os.environ.get('STORAGE') == 'S3' or DEBUG is False
# DB_RDS = True
print(DEBUG)
print(STORAGE_S3)

# /gori/django_app/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# /gori/
ROOT_DIR = os.path.dirname(BASE_DIR)
# STATIC - bower는 나중에 필요하면 주석 해제 해서 사용하셈
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# BOWER_DIR = os.path.join(ROOT_DIR, 'bower_components')
STATICFILES_DIRS = (
    STATIC_DIR,
    # BOWER_DIR,
)
# /gori/.conf-secret/
CONF_DIR = os.path.join(ROOT_DIR, '.conf-secret')
CONFIG_FILE_COMMON = os.path.join(CONF_DIR, 'settings_common.json')

# 디버그 모드일 경우 local, 아닐 경우 deploy 파일을 불러온다.
if DEBUG:
    CONFIG_FILE = os.path.join(CONF_DIR, 'settings_local.json')
else:
    CONFIG_FILE = os.path.join(CONF_DIR, 'settings_deploy.json')
config_common = json.loads(open(CONFIG_FILE_COMMON).read())
config = json.loads(open(CONFIG_FILE).read())

# common과 현재 사용설정 (local또는 deploy)를 합쳐줌
for key, key_dict in config_common.items():
    if not config.get(key):
        config[key] = {}
    for inner_key, inner_key_dict in key_dict.items():
        config[key][inner_key] = inner_key_dict

# AWS
AWS_ACCESS_KEY_ID = config['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config['aws']['secret_access_key']

AWS_S3_HOST = 's3.{}.amazonaws.com'.format(config['aws']['s3_region'])
AWS_S3_SIGNATURE_VERSION = config['aws']['s3_signature_version']
AWS_STORAGE_BUCKET_NAME = config['aws']['s3_storage_bucket_name']
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

# Static, Media storages
if STORAGE_S3:
    # Static files
    STATICFILES_STORAGE = 'config.storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    STATIC_URL = 'https://{custom_domain}/{staticfiles_location}/'.format(
        custom_domain=AWS_S3_CUSTOM_DOMAIN,
        staticfiles_location=STATICFILES_LOCATION,
    )
    # Media files
    DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = 'https://{custom_domain}/{mediafiles_location}/'.format(
        custom_domain=AWS_S3_CUSTOM_DOMAIN,
        mediafiles_location=MEDIAFILES_LOCATION
    )
else:
    STATIC_ROOT = os.path.join(ROOT_DIR, 'static_root')
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')

SECRET_KEY = config['django']['secret_key']
ALLOWED_HOSTS = config['django']['allowed_hosts']

# TEMPLATE
TEMPLATES_DIR = 'templates'

AUTH_USER_MODEL = 'member.GoriUser'

SITE_ID = 2

LOGIN_URL = '/admin/'
CALLBACK_URL = '/admin/'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    )
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # extension
    'django_extensions',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    # API 만들기 위한 프레임워크
    'rest_framework',
    # API 토큰
    'rest_framework.authtoken',
    # rest_framework 토큰 라이브러리
    'rest_auth',
    #
    'corsheaders',
    # aws s3
    'storages',

    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

    'member',
    'talent.apps.ClassConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
config_db = config['db']
DATABASES = {
    'default': {
        'ENGINE': config_db['engine'],
        'NAME': config_db['name'],
        'USER': config_db['user'],
        'PASSWORD': config_db['password'],
        'HOST': config_db['host'],
        'PORT': config_db['port'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True
