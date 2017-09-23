from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin


try:
    API_VERSION = settings.M.API_VERSION
except AttributeError:
    API_VERSION = 'v'


urlpatterns = [
    url('{0}/'.format(API_VERSION), include([
        url(r'', include('apps.indicators.urls')),
        url(r'^admin/', admin.site.urls),
    ])),
]
