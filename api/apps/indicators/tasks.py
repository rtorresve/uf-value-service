# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
import logging
import re

from bs4 import BeautifulSoup

from apps.indicators.models import UF
from apps.scrappers.indicatorsCrawl import get_values_by_years
from apps.snippets import utils
from apps.tasks.celery import app
from apps.snippets.utils import chunks
from django.db.utils import IntegrityError


PATTERN_DATE = '\d{2}.[A-Z][a-z]{2}.\d{4}'

logger = logging.getLogger(__name__)


@app.task
def get_historical_values(year_from, year_to):
    logger.info('start get_historical_values task')
    pattern = re.compile(PATTERN_DATE)
    for years in list(chunks(range(year_to, year_from - 1, -1), 5)):
        logger.info('getting historical for years {0}'.format(years))
        years_dict = get_values_by_years(years)
        for response in years_dict:
            logger.info('Saving records to year {0}'.format(response.get('year')))
            unity_values = []
            soup_d = BeautifulSoup(response.get('dates'), 'html.parser')
            soup_v = BeautifulSoup(response.get('values'), 'html.parser')
            for cel_d, cel_v in zip(soup_d.find_all('th'), soup_v.find_all('td')):
                date = cel_d.text.strip()
                value = cel_v.text.strip()
                if pattern.match(date):
                    date = utils.convert_to_date(date)
                    value = utils.convert_float_to_english(value)
                    unity_values.append(
                        UF(
                            value=value,
                            date=date,
                        ),
                    )
            try:
                UF.objects.bulk_create(unity_values)
            except IntegrityError as e:
                logger.warning('Integrity Error {0}'.format(e))
    logger.info('end get_historical_values task')
