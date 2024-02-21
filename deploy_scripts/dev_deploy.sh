#!/bin/bash
# Runs entire application stack on EC2 server (must be ran with ```bash deploy_scripts/deploy.sh``` from vacation_helper dir)

docker-compose -f docker/docker-compose-dev.yml up
