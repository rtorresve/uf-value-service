#!/usr/bin/env python
import _mysql_exceptions
import _mysql
import os
from time import sleep

flag = True

DB = os.environ.get('MYSQL_DATABASE')
HOST = os.environ.get('MYSQL_HOST', 'db')
PASSWORD = os.environ.get('MYSQL_PASSWORD')
USER = os.environ.get('MYSQL_USER')

while (flag):
    try:
        conn = _mysql.connect(db=DB, user=USER, passwd=PASSWORD, host=HOST)
        flag = False
    except _mysql_exceptions.OperationalError:
        print('MySql is unavailable - sleeping')
        sleep(1)
print('MySql is up - continuing...')
