from api.base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n_nb4sb14=^k(8y*m!fjxze8q*t836pz_l7kmtk*2%f)2#oba2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [ 'ciphernetron.com', 'api.ciphernetron.com', '.ciphernetron.com' ]
CSRF_TRUSTED_ORIGINS = [ 'http://ciphernetron.com', 'https://ciphernetron.com', 'https://*.ciphernetron.com', 'http://*.ciphernetron.com' ]
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Capstone',
        'USER': 'postgresql',
        'PASSWORD': 'password',
        'HOST': 'capstone_db',
        'PORT': '5432',
    }
}

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'https://ciphernetron.com',
    'http://ciphernetron.com',
    'https://api.ciphernetron.com',
    'http://api.ciphernetron.com',
]

CSRF_COOKIE_HTTPONLY = False
