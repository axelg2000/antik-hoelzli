from antik_hoelzli.shared_settings.dev_sqlite import *
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent

# Determine environment
ENVIRONMENT = os.getenv('DJANGO_ENV', 'development_sqlite')

print("ENVIRONMENT:", ENVIRONMENT)

if ENVIRONMENT == 'production_psql':
    from antik_hoelzli.shared_settings.prod_psql import *
elif ENVIRONMENT == 'production_sqlite':
    from antik_hoelzli.shared_settings.prod_sqlite import *
elif ENVIRONMENT == 'development_psql':
    from antik_hoelzli.shared_settings.dev_psql import *
elif ENVIRONMENT == 'development_sqlite':
    from antik_hoelzli.shared_settings.dev_sqlite import *
else:
    raise Exception(f"Unknown DJANGO_ENV: {ENVIRONMENT}")

print("DEBUG after loading:", DEBUG)
print("ALLOWED_HOSTS after loading:", ALLOWED_HOSTS)
print("DATABASES after loading:", DATABASES)