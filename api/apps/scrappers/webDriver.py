# -*- coding: utf-8 -*-
'''
Created on Sep 14, 2017

@author: rtorres
'''
import os

import milieu
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


WEBDRIVER_HEADER = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}  # noqa


def get_driver_browser():
    driver = None
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        m = milieu.init(path=os.path.join(base_dir, '../conf.json'))
    except FileNotFoundError:
        raise FileNotFoundError('I do not find the conf.json file')
    browser = m.BROWSER
    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'phantomjs':
        temp_header = 'phantomjs.page.customHeaders.{}'
        for key, value in enumerate(WEBDRIVER_HEADER):
            webdriver.DesiredCapabilities.PHANTOMJS[temp_header.format(key)] = value
        driver = webdriver.PhantomJS()
        driver.set_window_size(1280, 720)
    elif browser == 'remote':
        browser_path = m.BROWSER_URL
        driver = webdriver.Remote(
            command_executor=browser_path,
            desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
            keep_alive=False,
            browser_profile=FirefoxProfile())
        driver.maximize_window()
    else:
        raise Exception('browser undefined')
    if driver:
        driver.implicitly_wait(5)
    return driver
