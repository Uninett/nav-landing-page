import os

# Replaced by docker script on deploy
SECRET_KEY = ''

DEBUG = os.environ.get('DJANGO_DEBUG', '0').lower() in ('1', 'true', 'on', 'yes')
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'navlanding',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}