import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^&j)73vlsgig7+m(by7+13^3v!nl!e%q3owfuj#e1^#_r5^_v6'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'rbc.trendercom.net']
CSRF_TRUSTED_ORIGINS = ['https://rbc.trendercom.net']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')