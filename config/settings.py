"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG')
if DEBUG is False:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_REFERRER_POLICY = 'strict-origin'


    

ALLOWED_HOSTS = [
    'kevinarm.me',
    'www.kevinarm.me',
    '127.0.0.1',
    'localhost',
    'kevinarmportfolio-c1d3ab3aada9.herokuapp.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_recaptcha',
    'home',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
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
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),    
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Content Security Policy
# CSP_DEFAULT_SRC = ("'self'", "https://nyc3.digitaloceanspaces.com", "https://www.google.com/recaptcha/", "https://www.gstatic.com/recaptcha/", "https://www.google.com")
# CSP_IMG_SRC = ("'self'", "https://nyc3.digitaloceanspaces.com", "https://www.google.com", "https://www.gstatic.com/recaptcha/", "https://www.google.com/recaptcha/")
# CSP_STYLE_SRC = ("'self'", "https://nyc3.digitaloceanspaces.com", "https://www.google.com/recaptcha/", "https://www.gstatic.com/recaptcha/")
# CSP_SCRIPT_SRC = ("'self'", "https://nyc3.digitaloceanspaces.com", "https://www.google.com/recaptcha/", "https://www.gstatic.com/recaptcha/")
# CSP_FONT_SRC = ("'self'", "https://nyc3.digitaloceanspaces.com", "https://www.google.com/recaptcha/", "https://www.gstatic.com/recaptcha/")
# CSP_INCLUDE_NONCE_IN = ['script-src']
# CSP_REPORT_URI = '/csp-report/'
# CSP_REPORT_ONLY = False
# CSP_REPORTS_LOG = True
# CSP_REPORTS_LOG_LEVEL = 'warning'
# CSP_REPORTS_EMAIL_ADMINS = False
# CSP_REPORTS_EMAIL_ADMINS_FROM = 'CSP Reports <  >'
# CSP_REPORTS_EMAIL_ADMINS_TO = ['']
# CSP_REPORTS_EMAIL_ADMINS_SUBJECT = 'CSP Report'
# CSP_REPORTS_EMAIL_ADMINS_TEMPLATE = 'csp/email.html'
# CSP_REPORTS_EMAIL_ADMINS_HTML = True
# CSP_REPORTS_EMAIL_ADMINS_PLAIN = False
# CSP_REPORTS_SAVE = False
# CSP_REPORTS_LOG = True
# CSP_REPORTS_LOG_LEVEL = 'warning'
# CSP_REPORTS_LOG_FILENAME = 'csp-reports.log'
# CSP_REPORTS_LOG_MAXSIZE = 100 * 1024 * 1024
# CSP_REPORTS_LOG_BACKUPS = 10
# CSP_REPORTS_LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
# CSP_REPORTS_LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
# CSP_REPORTS_LOG_INTERVAL = 60 * 60
# CSP_REPORTS_LOG_BACKUP_COUNT = 10


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'static_root'
from .cdn.conf import *


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# Recaptcha settings
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')

