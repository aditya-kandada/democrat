# """
# Django settings for democrat project.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/1.6/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.6/ref/settings/
# """
#
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import path
#
#
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a8=$5+3+il+&9dmy#q2c0@m1o55mg#9*^oi(@09uxajpd3n&5g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


PROJECT_ROOT = path.abspath(path.dirname(__file__))
SITE_ROOT    = path.abspath(path.join(PROJECT_ROOT, path.pardir))

STATIC_URL ='/static/'

STATIC_ROOT = path.join(SITE_ROOT, 'static/')
# Application definition

STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, "/static/"),
)

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'democrat',
    'polls'
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',

)



ROOT_URLCONF = 'democrat.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'democrat.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    path.join(SITE_ROOT, 'templates/'),
    path.join(PROJECT_ROOT, 'templates/'),
)









ROOT_URLCONF = 'democrat.urls'

WSGI_APPLICATION = 'democrat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

ADMINS = (
    ('Aditya Kandada', 'aditya.kandada@carneylabs.com'),

)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'd6mpmo5m02gfle',
        'USER': 'wkkkjhhyxaadxp',
        'PASSWORD': 'bghRJeW6N211YxlirF6vjqDNI7',
        'HOST': 'ec2-54-197-237-231.compute-1.amazonaws.com',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




