"""
settngs/production.py
Production settings for humorproject.
"""

import os

from .common import *

DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.bierfeldt.me', # Allow domain and subdomains
    '.bierfeldt.me.', # Also allow FQDN and subdomains,
    ]
    
DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'humor_project',
                'USER': 'humor_project',
                'PASSWORD': os.environ["PROD_DB_PASS"],
                'HOST': 'localhost',
                'PORT': '',
            }
        }
        
SECRET_KEY = os.environ["PROD_SECRET_KEY"]
