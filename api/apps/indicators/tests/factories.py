# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
import factory
from factory.fuzzy import FuzzyDecimal, FuzzyDate
import datetime


class UFFactory(factory.django.DjangoModelFactory):
    value = FuzzyDecimal(0.5, 1.0, 2)
    date = FuzzyDate(start_date=datetime.date.today())

    class Meta:
        model = 'indicators.UF'
        django_get_or_create = ('date', )
