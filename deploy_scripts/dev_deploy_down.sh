#!/bin/bash
# Takes down dev application stack  (must be ran with ```bash deploy_scripts/dev_deploy_down.sh``` from vacation_helper dir)

docker-compose -f docker/docker-compose-dev.yml down
