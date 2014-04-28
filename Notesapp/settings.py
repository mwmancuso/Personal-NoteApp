"""
Django settings for Notesapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
from Notesapp.environment import SECRET_KEY, DATABASES, DEBUG,\
    TEMPLATE_DEBUG, LOGGING_FILENAME, EMAIL_HOST, EMAIL_PORT,\
    EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS, SITE_PATH,\
    STATIC_ROOT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Fake ugettext function for translations
_ = lambda s: s

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Secret key is configured in environment file

# SECURITY WARNING: don't run with debug turned on in production!
# Debug settings in environment file

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'authentication',
    'errors',
    'meta',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Notesapp.urls'
WSGI_APPLICATION = 'Notesapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# Databases are configured in environment settings

DATABASE_ROUTERS = ['Notesapp.routers.AppRouter']

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'Notesapp/locale/'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Logging
# https://docs.djangoproject.com/en/1.6/topics/logging/

if DEBUG:
    LOGGING_LEVEL = 'DEBUG'
else:
    LOGGING_LEVEL = 'WARNING'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d '+\
                      '%(thread)d %(message)s',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGGING_FILENAME,
            'maxBytes': 1048576,
            'backupCount': 30,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propogate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['file'],
            'level': LOGGING_LEVEL,
            'propogate': False,
        },
        '': {
            'handlers': ['file'],
            'level': LOGGING_LEVEL,
            'propogate': False,
        }
    },
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates')
)