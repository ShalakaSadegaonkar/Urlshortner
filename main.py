#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app,db
import url.views
import url.models

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
