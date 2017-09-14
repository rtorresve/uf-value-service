# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
import milieu
import os
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings

try:
    M = milieu.init(path='/app/conf.json')
except FileNotFoundError:
    M = milieu.init()

DJANGO_ENV = M.DJANGO_ENV or 'dev'

if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'conf.settings.{0}'.format(DJANGO_ENV))  # pragma: no cover


app = Celery('tasks', broker=settings.M.CELERY_BROKER_URL)

app.autodiscover_tasks(['apps.indicators'])


class CeleryConfig(AppConfig):
    name = 'apps.tasks'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.
        app.config_from_object('django.conf:settings')
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)

        if hasattr(settings, 'RAVEN_CONFIG'):
            # Celery signal registration

            from raven import Client as RavenClient
            from raven.contrib.celery import register_signal as raven_register_signal
            from raven.contrib.celery import register_logger_signal as raven_register_logger_signal

            raven_client = RavenClient(dsn=settings.RAVEN_CONFIG['dsn'])
            raven_register_logger_signal(raven_client)
            raven_register_signal(raven_client)
