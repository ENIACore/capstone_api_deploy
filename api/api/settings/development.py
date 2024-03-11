from api.base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n_nb4sb14=^k(8y*m!fjxze8q*t836pz_l7kmtk*2%f)2#oba2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow all localhost connections (drf admin and react)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
# Trust csrf tokens from react app on port 5173
CSRF_TRUSTED_ORIGINS = ['http://localhost:5173', 'http://127.0.0.1:5173', 'https://localhost:5173', 'https://127.0.0.1:5173']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dev_db' / 'db.sqlite3',
    }
}

# Allow credentials from approved CORS origins
CORS_ALLOW_CREDENTIALS = True
# Allow CORS requests from localhost:5173 (and port 8000 for drf admin, optional)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
