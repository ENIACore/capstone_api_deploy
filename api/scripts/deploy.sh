#!/bin/bash
# Used by docker image to start api using wsgi                                     

PORT=${PORT:="8080"}
WEB_COUNT=${WEB_COUNT:="2"}

gunicorn api.wsgi -b 0.0.0.0:$PORT -w $WEB_COUNT
