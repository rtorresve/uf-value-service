from rest_framework_json_api import serializers

from apps.indicators.models import UF


class UFSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UF
        fields = ('date', 'value')
