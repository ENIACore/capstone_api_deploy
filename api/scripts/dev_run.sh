#!/bin/bash
# Runs api locally without a container and makes necessary commands before doing so (assumes that the db container is running already)

python3 manage.py collectstatic --no-input
python3 manage.py migrate --no-input

export DJANGO_SUPERUSER_PASSWORD=uncommonpassword1234
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@email.com

python3 manage.py createsuperuser --noinput
python3 manage.py runserver
