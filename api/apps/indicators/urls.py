from django.conf.urls import url, include
from rest_framework import routers

from apps.indicators.views import UFViewSet


router = routers.DefaultRouter()
router.register(r'uf', UFViewSet)
UFListView = UFViewSet.as_view({'get': 'list'})

urlpatterns = [
    url(r'^indicators/', include(router.urls)),
    url(r'^uf/list$', UFListView),
]
