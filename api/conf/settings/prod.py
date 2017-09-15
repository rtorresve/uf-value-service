# -*- coding: utf-8 -*-
'''
Created on Sep 12, 2017

@author: rtorres
'''
import dj_database_url

import raven

from .base import *


SECRET_KEY = M.SECRET_KEY

INSTALLED_APPS += ['raven.contrib.django.raven_compat', ]

DEBUG = False

ALLOWED_HOSTS = M.ALLOWED_HOSTS

INSTALLED_APPS += [
    'gunicorn',
    'raven.contrib.django.raven_compat',
]

DATABASES = {'default': dj_database_url.config(default=M.DATABASE_URL)}

SENTRY_CLIENT = 'raven.contrib.django.raven_compat.DjangoClient'

RAVEN_CONFIG = {
    'dsn': M.DJANGO_SENTRY_DSN,
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir))}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry', ],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
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
            'formatter': 'verbose'
        }
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
