"""
Django settings for medical_app project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
from rest_framework.settings import api_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(j46!_h^x1(cn4dal^bqb%)re-+j5sq6%!b%see&gruvx*tk^h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['cc86-102-88-71-248.ngrok-free.app','127.0.0.1']

ALLOWED_HOSTS = ['8813-102-89-41-130.ngrok-free.app','127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "knox",
    'api.apps.ApiConfig',
    'events.apps.EventsConfig',
    'users.apps.UsersConfig',
    'platforms.apps.PlatformsConfig',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medical_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'medical_app.wsgi.application'


AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    "DATETIME_FORMAT":"%d/%b/%Y %H:%M",
    "DATE_FORMAT":"%d/%b/%Y",
    
}

# REST_KNOX = {
#   'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
#   'AUTH_TOKEN_CHARACTER_LENGTH': 64,
#   'TOKEN_TTL': timedelta(hours=12),
#   'USER_SERIALIZER': 'knox.serializers.UserSerializer',
#   'TOKEN_LIMIT_PER_USER': None,
#   'AUTO_REFRESH': False,
#   'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
# }



KNOX_TOKEN_MODEL = 'knox.AuthToken'

REST_KNOX = {
  'SECURE_HASH_ALGORITHM': 'hashlib.sha512',
  'AUTH_TOKEN_CHARACTER_LENGTH': 64,
  'TOKEN_TTL': timedelta(hours=12),
  'USER_SERIALIZER': 'knox.serializers.UserSerializer',
  'TOKEN_LIMIT_PER_USER': None,
  'AUTO_REFRESH': False,
  'AUTO_REFRESH_MAX_TTL': None,
  'MIN_REFRESH_INTERVAL': 60,
  'AUTH_HEADER_PREFIX': 'Token',
  'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
  'TOKEN_MODEL': 'knox.AuthToken',
}





CORS_ORIGIN_WHITELIST = ['https://8813-102-89-41-130.ngrok-free.app','http://localhost:8081','http://localhost:8082']


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
