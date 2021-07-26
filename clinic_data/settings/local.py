from .base import *
#from .json import getSecret
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getSecret("DB_NAME"),
        'USER':getSecret("DB_USER"),
        "PASSWORD":getSecret("DB_PASS"),
        "HOST":"localhost",
        "PORT":"5432",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#This part is for production use only
STATIC_ROOT = BASE_DIR /'staticfiles'
STATICFILES_DIR=[
    BASE_DIR/'static',
]

MEDIA_URL='media/'
MEDIA_ROOT= BASE_DIR/'media'