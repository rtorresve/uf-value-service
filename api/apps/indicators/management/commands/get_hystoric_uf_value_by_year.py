# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
import re
import logging

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from apps.scrappers.indicatorsCrawl import get_values_by_years
from apps.snippets import validators as val
from apps.snippets import utils

PATTERN_DATE = '\d{2}.[A-Z][a-z]{2}.\d{4}'

logger = logging.getLogger('commands')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--from',
            '-f',
            type=int,
            dest='year_from',
            help='The year is a integer between 1977 - 2017',
        )
        parser.add_argument(
            '--to',
            '-t',
            type=int,
            dest='year_to',
            help='The year is a integer between 1977 - 2017',
        )

    def handle(self, **options):
        def splits(l, n):
            [l[x: x + n] for x in range(0, len(l), n)]
        try:
            year_to = options['year_to']
            year_from = options['year_from']
            val.validate_input_year(year_from)
            val.validate_input_year(year_to)
            val.validate_order_years(year_to, year_from)
            years_list = list(range(year_to, year_from - 1, -1))
            for years in splits(years_list, 5):
                years_dict = get_values_by_years(years)
                for response in years_dict:
                    soup = BeautifulSoup(response.get('dates'), 'html.parser')
                    dates = []
                    values = []
                    pattern = re.compile(PATTERN_DATE)
                    for cel in soup.find_all('th'):
                        dates.append(cel.text.strip())
                    soup = BeautifulSoup(response.get('values'), 'html.parser')
                    for cel in soup.find_all('td'):
                        values.append(cel.text.strip())
                    for i in range(len(dates)):
                        if pattern.match(dates[i]):
                            date = utils.convert_date_to_english(dates[i])
                            value = utils.convert_float_to_english(values[i])
                            print(date, value)
        except KeyError as e:
            logger.error('ERROR: {}'.format(e), exc_info=e, stack_info=True)
            return
        finally:
            logger.info('Finished command')
