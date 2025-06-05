from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = [os.getenv('PRODUCTION_HOST', 'yourdomain.com')]

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