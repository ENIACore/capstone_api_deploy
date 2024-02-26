#!/bin/bash
# Runs postgressql container for development purposes (must be ran using ```bash scripts/dev_db_run.sh```)

docker run -d \
    --name capstone_development_db \
    --restart always \
    -v db_dev_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    -e POSTGRES_DB=Capstone \
    -e POSTGRES_USER=postgresql \
    -e POSTGRES_PASSWORD=password \
    postgres:latest

