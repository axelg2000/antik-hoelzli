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