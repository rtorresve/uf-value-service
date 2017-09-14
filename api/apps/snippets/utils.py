# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
from datetime import datetime


def convert_to_date(date_str):
    date_str = date_str.replace('Ene', 'Jan').replace('Abr', 'Apr')
    date_str = date_str.replace('Ago', 'Aug').replace('Dic', 'Dec')
    return datetime.strptime(date_str, '%d.%b.%Y')


def convert_float_to_english(float_str):
    float_str = float_str.replace('.', '').replace(',', '.')
    return float(float_str)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
