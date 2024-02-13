#!/bin/bash

set -ueo pipefail


./python manage.py collectstatic --no-input
./python manage.py migrate --no-input
