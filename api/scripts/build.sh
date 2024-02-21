#!/bin/bash
# Builds docker image (must be ran using ```bash scripts/build.sh```)

docker build . -f Dockerfile -t jayaanim/capstone_api:latest
