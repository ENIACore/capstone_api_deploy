#!/bin/bash
# Runs api locally without a container and makes necessary commands before doing so (assumes that the db container is running already)

export DJANGO_SETTINGS_MODULE=api.settings.development

python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input

python3 manage.py get_or_create_superuser admin admin@email.com uncommonpassword1234

python3 manage.py runserver
