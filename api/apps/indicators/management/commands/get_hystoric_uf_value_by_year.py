# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
import logging

from django.core.management.base import BaseCommand

from apps.indicators.tasks import get_historical_values
from apps.snippets import validators as val

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
        try:
            year_to = options['year_to']
            year_from = options['year_from']
            val.validate_input_year(year_from)
            val.validate_input_year(year_to)
            val.validate_order_years(year_to, year_from)
            get_historical_values.delay(year_from, year_to)
        except KeyError as e:
            logger.error('ERROR: {}'.format(e), exc_info=e, stack_info=True)
            return
        finally:
            logger.info('Finished command')
