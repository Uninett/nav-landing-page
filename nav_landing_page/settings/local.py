# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wd#p5+pca*5&@sgz(38ef9ku8vte^^t#lq*x#za3h0251@)@ds'

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

