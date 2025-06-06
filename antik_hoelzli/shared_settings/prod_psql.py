# prod.py
from .base import *
import os
import dj_database_url

INSTALLED_APPS += ['storages']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'eu-central-1')  # replace with your region

# Optional: make uploaded media publicly accessible
AWS_QUERYSTRING_AUTH = False

# Optional: set default ACL to public-read
AWS_DEFAULT_ACL = 'public-read'

DEBUG = True
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