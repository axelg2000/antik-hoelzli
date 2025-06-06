# prod.py
from .base import *
import os
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = [os.getenv('PRODUCTION_HOST', 'yourdomain.com')]

# Use Heroku DATABASE_URL if available, fallback to env vars
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', 'antik_hoelzli'),
            'USER': os.getenv('POSTGRES_USER', 'axel'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'DB38920Crolles.'),
            'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
            'PORT': os.getenv('POSTGRES_PORT', '5432'),
        }
    }