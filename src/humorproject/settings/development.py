"""
settngs/development.py
Development settings for humorproject.

The development environment is light and local. All data is stored underneath
the development virtualenv.
"""
import os

from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "humorproject",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}

INTERNAL_IPS = ("127.0.0.1",)
SECRET_KEY = 's'

if 'HUMORPROJECT_CONFIG_PATH' in os.environ:
    execfile(os.environ['HUMORPROJECT_CONFIG_PATH'])
