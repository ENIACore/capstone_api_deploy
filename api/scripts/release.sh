#!/bin/bash
# Used by image to make configs before running api

set -ueo pipefail

python3 manage.py collectstatic --no-input
python3 manage.py migrate --no-input

export DJANGO_SUPERUSER_PASSWORD=uncommonpassword1234
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@email.com

python3 manage.py createsuperuser --noinput

python3 manage.py runserver
