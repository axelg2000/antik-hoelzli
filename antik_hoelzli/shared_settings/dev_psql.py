from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'antik_hoelzli',
        'USER': 'axel',
        'PASSWORD': 'DB38920Crolles.',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}