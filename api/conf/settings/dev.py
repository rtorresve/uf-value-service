# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
from .base import *  # noqa

DEBUG = M.DJANGO_DEBUG or True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = ',2c^~jZkmoBoSkDPh&RP6c{~dg*aCEGf|}{(qT.u,M!7C,)w?:'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]


import socket
import os
# tricks to have debug toolbar when developing with docker
if os.environ.get('USE_DOCKER') == 'yes':
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + '1']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

INSTALLED_APPS += ['django_extensions', ]

CELERY_ALWAYS_EAGER = True