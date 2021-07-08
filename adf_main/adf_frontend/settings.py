# jknejk
# this change is made by satyam
# this change is made by satyam-adf
# this change is made by satyam-adf
"""
Django settings for adf_frontend project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'syvjpg(n7mdg(e3qz4%(z&%k&)+t@m)kt0c80@1827ppcew&-3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
     
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'upload',
    'search',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.LoginCheckMiddleWare.LoginCheckMiddleWare',
]

ROOT_URLCONF = 'adf_frontend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'adf_frontend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',           #'django.db.backends.sqlite3',
#         'NAME':   'adf_main',              # DB name
#         #'USER': 'root',               # DB User name <optional>
#     }
# }

DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'adf_main',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'mongodb+srv://analytics:analytics-password@mflix.uxx0e.mongodb.net/mflix?retryWrites=true&w=majority'
            }  
        }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False                 
DATETIME_FORMAT = 'Y-m-d H:i:s'

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')


MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")


AUTH_USER_MODEL="users.CustomUser"
AUTHENTICATION_BACKEND = ['users.EmailBackEnd.EmailBackEnd']

# EMAIL_BACKEND="django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH=os.path.join(BASE_DIR,"sent_mails")

EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_HOST_USER="satyamprakashiitk2022@gmail.com"# put host email id
EMAIL_HOST_PASSWORD="Saty123@"
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL="ADF Management System <satyamprakashiitk2022@gmail.com>"# put host email id

#............#
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#............#
CORS_ORIGIN_ALLOW_ALL = True

# Activate Django-Heroku.
django_heroku.settings(locals())
