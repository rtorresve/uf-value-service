# -*- coding: utf-8 -*-
'''
Created on Sep 10, 2017

@author: rtorres
'''
from decimal import Decimal
from filters.schema import base_query_params_schema
from filters.validations import DatetimeWithTZ
from voluptuous.error import Invalid


def DecimalValidation(msg=None):  # noqa
    '''
    Checks whether a value is :
        - a valid decimal object with timezone.
    '''
    def fn(value):
        try:
            value = Decimal(value)
            return value
        except Exception:
            raise Invalid('<{0}> is not a valid decimal.'.format(value))
    return fn


uf_query_schema = base_query_params_schema.extend(
    {
        'value': DecimalValidation(),
        'date': DatetimeWithTZ(),
    })
