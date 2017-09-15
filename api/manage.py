#!/usr/bin/env python
import milieu
import os
import sys
from builtins import FileNotFoundError

try:
    M = milieu.init(path='/app/conf.json')
except FileNotFoundError:
    M = milieu.init()

DJANGO_ENV = M.DJANGO_ENV or 'dev'

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings.{0}'.format(DJANGO_ENV))
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?")
        raise
    current_path = os.path.dirname(os.path.abspath(__file__))
    execute_from_command_line(sys.argv)
