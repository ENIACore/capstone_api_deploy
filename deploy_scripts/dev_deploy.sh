#!/bin/bash
# Runs entire application stack locally for testing (must be ran with ```bash deploy_scripts/dev_deploy.sh``` from vacation_helper dir)

docker-compose -f docker/docker-compose-dev.yml up -d --build
