"""
settngs/production.py
Production settings for humorproject.
"""

import os

from .common import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.lensplease.com', # Allow domain and subdomains
    '.lensplease.com.', # Also allow FQDN and subdomains
    '.shutterclub.co',
    '.shutterclub.co.',
    ]
    
DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'lensplease',
                'USER': 'lensplease',
                'PASSWORD': os.environ["PROD_DB_PASS"],
                'HOST': 'localhost',
                'PORT': '',
            }
        }
        
SECRET_KEY = os.environ["PROD_SECRET_KEY"]