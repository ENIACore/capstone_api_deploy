#!/bin/bash


PORT=${PORT:="8080"}
WEB_COUNT=${WEB_COUNT:="2"}


gunicorn config.wsgi -b 0.0.0.0:$PORT -w $WEB_COUNT
