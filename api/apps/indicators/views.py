from filters.mixins import FiltersMixin
from rest_framework import viewsets

from apps.indicators.models import UF
from apps.indicators.serializers import UFSerializer
from apps.indicators.validations import uf_query_schema


class UFViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = UF.objects.all()
    serializer_class = UFSerializer
    ordering = ('date',)
    filter_validation_schema = uf_query_schema
    filter_mappings = {
        'date': 'date',
        'value': 'value',
    }

    def get_queryset(self):
        query_params = self.request.query_params
        url_params = self.kwargs
        queryset_filters = self.get_db_filters(url_params, query_params)
        db_filters = queryset_filters['db_filters']
        queryset = UF.objects.all()
        return queryset.filter(**db_filters)
