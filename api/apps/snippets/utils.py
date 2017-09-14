# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''


def convert_date_to_english(date_str):
    date_str.replace('Ene', 'Jan')
    date_str.replace('Abr', 'Apr')
    date_str.replace('Ago', 'Aug')
    date_str.replace('Dic', 'Dec')
    return date_str


def convert_float_to_english(float_str):
    float_str.replace('.', '')
    float_str.replace(',', '.')
    return float_str
