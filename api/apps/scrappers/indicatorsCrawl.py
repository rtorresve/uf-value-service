# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from apps.scrappers import constants as c
from apps.scrappers.webDriver import get_driver_browser


def find_current_uf_value():
    driver = get_driver_browser()
    driver.get(c.CENTRAL_BANK_PAGE)
    span = driver.find_element(
        by=By.XPATH,
        value=c.UF_VALUE_SPAN_XPATH)
    value = span.text.replace('.', '').replace(',', '.')
    driver.close()
    return value


def get_values_by_years(years):
    response = []
    try:
        driver = get_driver_browser()
        driver.get(c.CENTRAL_BANK_PAGE)
        driver.get(c.STADISTICS_PAGE_URL)
        driver.find_element(
            by=By.ID,
            value=c.LINK_HISTORICAL_ID).click()
        driver.get(c.UF_DATA_URL)
        if 'error' in driver.title.lower():
            driver.find_element(
                by=By.ID,
                value=c.BUTTON_ERROR_RETURN_ID).click()
            driver.find_element(
                by=By.ID,
                value=c.LINK_HISTORICAL_ID).click()
            driver.get(c.UF_DATA_URL)
        for year in years:
            sel = driver.find_element(By.ID, c.YEAR_SELECT_ID)
            select = Select(sel)
            select.select_by_value(str(year))
            sleep(5)
            row_header = driver.find_element(By.XPATH, c.DAYS_TH_XPATH)
            row_data = driver.find_element(By.XPATH, c.DATA_TR_XPATH)
            response.append(
                {
                    'year': year,
                    'dates': row_header.get_attribute('innerHTML'),
                    'values': row_data.get_attribute('innerHTML'),
                })
    except Exception as e:
        print(e)
    finally:
        driver.close()
    return response
