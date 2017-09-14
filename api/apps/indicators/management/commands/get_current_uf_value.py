# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
from django.core.management.base import BaseCommand

from apps.scrappers.indicatorsCrawl import find_current_uf_value

import logging


logger = logging.getLogger('commands')


class Command(BaseCommand):

    def handle(self, **options):
        print(find_current_uf_value())
        logger.info('Finished command')
