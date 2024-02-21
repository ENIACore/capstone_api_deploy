FROM python:3.11-bullseye 

# Base dependencies
RUN apt-get update && apt-get install -y \
    tree parallel gettext vim git wget lsb-release

# Create app dir
WORKDIR /api

# Custom system dependencies
ADD scripts/ /api/
RUN bash install.sh

# Python dependencies
ADD requirements.txt /api/
RUN python3 -m pip install -r requirements.txt

# Add everything else
ADD . /api/

# Default command
CMD bash scripts/release.sh && bash scripts/deploy.sh
