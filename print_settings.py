import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'antik_hoelzli.settings')

import django
django.setup()

from django.conf import settings
import importlib

# Import the actual settings module
settings_module = importlib.import_module(os.environ['DJANGO_SETTINGS_MODULE'])

print("Loaded settings module file:", settings_module.__file__)
print("FINAL DEBUG:", settings.DEBUG)
print("FINAL ALLOWED_HOSTS:", settings.ALLOWED_HOSTS)
print("FINAL DATABASES:", settings.DATABASES)