#!/bin/bash
# Runs docker image locally (must be ran with ```bash scripts/dev_run.sh``` from api dir)
# Binds to port 80
# Names container capstone_api

docker run -p 80:8080 -d --name capstone_api jayaanim/capstone_api:latest
