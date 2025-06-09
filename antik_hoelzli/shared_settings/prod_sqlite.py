from .base import *
import os
from pathlib import Path

DEBUG = False
ALLOWED_HOSTS = [os.getenv('PRODUCTION_HOST', 'yourdomain.com')]

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Adjust if needed

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}