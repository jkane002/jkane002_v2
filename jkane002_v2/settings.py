"""
Django settings for jkane002_v2 project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JKANE002_V2_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')

ALLOWED_HOSTS = ['127.0.0.1', 'jkaneshiro.herokuapp.com', 'jkaneshiro.me' , 'www.jkaneshiro.me']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
    'blog.apps.BlogConfig',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jkane002_v2.urls'

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

WSGI_APPLICATION = 'jkane002_v2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-static-files-during-development
STATIC_ROOT = os.path.join(BASE_DIR, 'base/staticfiles')
STATIC_URL = '/staticfiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'base/static/images/')
MEDIA_URL = '/images/'

# AWS
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') 
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

if DEBUG:
    # Stripe API Test Keys
    STRIPE_PK = os.environ.get('STRIPE_TEST_PK')
    STRIPE_SK = os.environ.get('STRIPE_TEST_SK')

    # Stripe Price ID API Test Keys
    FULL_1_WEEK = os.environ.get('FULL_1_WEEK_TEST')
    FULL_5_WEEKS = os.environ.get('FULL_5_WEEKS_TEST')
    FULL_10_WEEKS = os.environ.get('FULL_10_WEEKS_TEST')
    FULL_15_WEEKS = os.environ.get('FULL_15_WEEKS_TEST')
    FULL_20_WEEKS = os.environ.get('FULL_20_WEEKS_TEST')
    
    # TODO: Figure out weekly subscription
    # WEEKLY_SUB = os.environ.get('WEEKLY_SUB_TEST')
else:
    # Stripe API Live Keys
    STRIPE_PK = os.environ.get('STRIPE_LIVE_PK')
    STRIPE_SK = os.environ.get('STRIPE_LIVE_SK')

    # Stripe Price ID API Test Keys
    FULL_1_WEEK = os.environ.get('FULL_1_WEEK_LIVE')
    FULL_5_WEEKS = os.environ.get('FULL_5_WEEKS_LIVE')
    FULL_10_WEEKS = os.environ.get('FULL_10_WEEKS_LIVE') 
    FULL_15_WEEKS = os.environ.get('FULL_15_WEEKS_LIVE') 
    FULL_20_WEEKS = os.environ.get('FULL_20_WEEKS_LIVE') 
    
    # TODO: Figure out weekly subscription
    # WEEKLY_SUB = os.environ.get('WEEKLY_SUB_LIVE') 

django_heroku.settings(locals())
