# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'change-this-in-production'

DEBUG = True
TEMPLATE_DEBUG = DEBUG 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

