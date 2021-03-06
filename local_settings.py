# Graphite local_settings.py

from os import getenv, urandom

SECRET_KEY = getenv('SECRET_KEY', urandom(24).encode('hex'))

STORAGE_DIR = getenv('STORAGE_DIR')
GRAPHITE_ROOT = '/var/graphite'
WEBAPP_DIR = '/usr/local/webapp/'

LOG_DIR = getenv('LOG_DIR')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'graphite': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

DATABASES = {
    'default': {
        'NAME': getenv('DATABASE_NAME', 'graphite'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': getenv('DATABASE_USER', 'graphite'),
        'PASSWORD': getenv('DATABASE_PASSWORD', 'graphite'),
        'HOST': getenv('DATABASE_HOST', 'localhost'),
        'PORT': '',
    },
}

try:
    from graphite.custom_settings import *
except ImportError:
    pass
