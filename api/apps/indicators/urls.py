from django.conf.urls import url, include
from rest_framework import routers

from apps.indicators.views import UFViewSet


router = routers.DefaultRouter()
router.register(r'uf', UFViewSet)

urlpatterns = [
    url(r'^indicators/', include(router.urls)),
]
