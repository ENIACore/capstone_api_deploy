FROM python:3.11-bullseye 

# Base dependencies
RUN apt-get update && apt-get install -y \
    tree parallel gettext vim git wget lsb-release

# Custom system dependencies
ADD scripts/ /
RUN bash install.sh

# Python dependencies
ADD requirements.txt /
RUN python3 -m pip install -r requirements.txt

# Add everything else
ADD . /

# Collect static and migrate
RUN bash release.sh

# Run wsgi server
CMD ["scripts/deploy.sh"]
