"""
Django settings for puppleApplication project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

from puppleApplication.properties.base import BaseProperties
from puppleApplication.properties.production import ProductionProperties


def get_properties_by_env() -> BaseProperties:
    env = os.environ.get('ENV', 'local')
    if env == 'local':
        return BaseProperties()
    elif env == 'production':
        return ProductionProperties()


activeProperties = get_properties_by_env()

BASE_DIR = activeProperties.BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = activeProperties.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = activeProperties.DEBUG

LOGGING = activeProperties.LOGGING

ALLOWED_HOSTS = activeProperties.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = activeProperties.INSTALLED_APPS

MIDDLEWARE = activeProperties.MIDDLEWARE

ROOT_URLCONF = activeProperties.ROOT_URLCONF

TEMPLATES = activeProperties.TEMPLATES

WSGI_APPLICATION = activeProperties.WSGI_APPLICATION


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = activeProperties.DATABASES


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = activeProperties.AUTH_PASSWORD_VALIDATORS

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = activeProperties.LANGUAGE_CODE

TIME_ZONE = activeProperties.TIME_ZONE

USE_I18N = activeProperties.USE_I18N

USE_L10N = activeProperties.USE_L10N

USE_TZ = activeProperties.USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS = activeProperties.STATICFILES_DIRS

STATIC_URL = activeProperties.STATIC_URL
STATIC_ROOT = activeProperties.STATIC_ROOT

MEDIA_URL = activeProperties.MEDIA_URL
MEDIA_ROOT = activeProperties.MEDIA_ROOT

CORS_ALLOW_ALL_ORIGINS = activeProperties.CORS_ALLOW_ALL_ORIGINS
CORS_REPLACE_HTTPS_REFERER = activeProperties.CORS_REPLACE_HTTPS_REFERER
