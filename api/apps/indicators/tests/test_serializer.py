# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
import datetime

from django.test.testcases import TestCase

from apps.indicators.models import UF


class TestUfSerializer(TestCase):

    def setUp(self):
        self.uf = UF.objects.create(
            date=datetime.date.today(),
            value=200.09)

    '''
    def test_data_rigth_format(self):
        serializer = UFSerializer(isntance=self.uf)
        expected_data = {
            'type': format_resource_type('UF'),
            'id': str(self.uf.id),
            'attributtes': {
                'date': datetime.date.today().strftime('%y-%m-%d'),
                'value': '200.09'}}
        assert serializer.data == expected_data
    '''
