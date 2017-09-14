# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
from datetime import datetime


def validate_input_year(year):
    """
    :param int:
    """
    try:
        current = datetime.now().year
        if not 1977 <= year <= current:
            raise ValueError('The year range is between 1977 - {0}'.format(current))
    except ValueError as e:
        raise e


def validate_order_years(year_to, year_from):
    """
    :param int: int:
    """
    if not year_to > year_from:
        raise ValueError('Verify the years order.')
