#!/bin/bash
# Used by image to make configs before running api

set -ueo pipefail

python3 manage.py collectstatic --no-input

python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input

python3 manage.py get_or_create_superuser admin admin@email.com uncommonpassword1234 
