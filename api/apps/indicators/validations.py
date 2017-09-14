# -*- coding: utf-8 -*-
'''
Created on Sep 10, 2017

@author: rtorres
'''
from filters.schema import base_query_params_schema
from filters.validations import DatetimeWithTZ


uf_query_schema = base_query_params_schema.extend(
    {
        'value': float,
        'date': DatetimeWithTZ(),
    })
