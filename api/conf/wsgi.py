"""
WSGI config for deathsdancing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import milieu


try:
    M = milieu.init(path='/app/conf.json')
except FileNotFoundError:
    M = milieu.init()

DJANGO_ENV = M.DJANGO_ENV or 'dev'

if DJANGO_ENV is 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings.prod')
    from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings.base')

application = get_wsgi_application()

if DJANGO_ENV is 'prod':
    application = Sentry(application)
