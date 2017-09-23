# -*- coding: utf-8 -*-
'''
Created on Sep 12, 2017

@author: rtorres
'''
import milieu
import os

from conf.settings.base import *  # noqa
from builtins import FileNotFoundError

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    M = milieu.init(path=os.path.join(BASE_DIR, '../conf.json'))
except FileNotFoundError:
    raise FileNotFoundError('I do not find the conf.json file')
SECRET_KEY = M.SECRET_KEY

CELERY_ALWAYS_EAGER = M.CELERY_ALWAYS_EAGER
CELERY_ALWAYS_EAGER = False
CELERY_BROKER_URL = M.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_BROKER_URL = M.CELERY_BROKER_URL or 'django://'

if CELERY_BROKER_URL == 'django://':
    CELERY_RESULT_BACKEND = 'redis://'
else:
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL


DEBUG = False

ALLOWED_HOSTS = M.ALLOWED_HOSTS

INSTALLED_APPS += [  # noqa
    'gunicorn',
    'raven.contrib.django.raven_compat',
]

RAVEN_MIDDLEWARE = ['raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware']
MIDDLEWARE = RAVEN_MIDDLEWARE + MIDDLEWARE  # noqa

DATABASES = {'default': dj_database_url.config(default=M.DATABASE_URL)}  # noqa

SENTRY_CLIENT = 'raven.contrib.django.raven_compat.DjangoClient'
SENTRY_CELERY_LOGLEVEL = M.DJANGO_SENTRY_LOG_LEVEL

RAVEN_CONFIG = {
    'dsn': M.DJANGO_SENTRY_DSN,
    'CELERY_LOGLEVEL': SENTRY_CELERY_LOGLEVEL}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry', ],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '  # noqa
                      '%(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console', ],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console', ],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console', ],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'sentry', ],
            'propagate': False,
        },
    },
}
