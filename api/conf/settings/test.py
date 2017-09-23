'''
Test settings

- Used to run tests fast on the continuous integration server and locally
'''
from conf.settings.base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
# Turn debug off so tests run faster
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False  # noqa

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = 'CHANGEME!!!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db3',
    },
}

# CACHING
# ------------------------------------------------------------------------------
# Speed advantages of in-memory caching without having to run Memcached
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    },
}

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# PASSWORD HASHING
# ------------------------------------------------------------------------------
# Use fast password hasher so tests run faster
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# TEMPLATE LOADERS
# ------------------------------------------------------------------------------
# Keep templates in memory so tests run faster
TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa
    ['django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ], ],
]

CELERY_ALWAYS_EAGER = True
