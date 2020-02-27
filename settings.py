import os

DB_USERNAME = 'raees'
DB_PASSWORD = 'raees'
DB_DATABASE_NAME = 'shortener'
DB_HOST = os.getenv('IP', '127.0.0.1')
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (
    DB_USERNAME, DB_PASSWORD, DB_HOST, DB_DATABASE_NAME)
