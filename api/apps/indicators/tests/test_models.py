# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
from test_plus.test import TestCase
from apps.indicators.tests.factories import UFFactory
import datetime


class TestUF(TestCase):

    def setUp(self):
        self.uf = UFFactory()

    def test_get_date(self):
        assert self.uf.date == datetime.date.today()

    def test_value_upper(self):
        assert self.uf.value < 1.1

    def test_value_lower(self):
        assert self.uf.value > 0.49
