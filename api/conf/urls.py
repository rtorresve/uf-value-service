from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url('{0}/'.format(settings.M.API_VERSION), include([
        url(r'', include('apps.indicators.urls')),
        url(r'^admin/', admin.site.urls),
    ])),
]
