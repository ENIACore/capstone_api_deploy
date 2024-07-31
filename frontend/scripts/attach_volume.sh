#!/bin/bash

docker volume rm frontend_build

docker pull jayaanim/capstone_frontend:latest

docker run --rm -v frontend_build:/app/build jayaanim/capstone_frontend:latest

