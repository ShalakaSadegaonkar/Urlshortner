#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:04:47 2020

@author: Shalaka.Sadegaonkar
"""


import os
import sys

DB_USERNAME = 'short'
DB_PASSWORD = 'root'
DB_DATABASE_NAME = 'shortener'
DB_HOST = os.getenv('IP', '127.0.0.1')
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = '<$üP3rPazzWø£D>'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (
    DB_USERNAME, DB_PASSWORD, DB_HOST, DB_DATABASE_NAME)

