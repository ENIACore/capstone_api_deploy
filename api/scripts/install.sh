#!/bin/bash
# Installs needed image libraries

set -eou pipefail

apt-get -y install binutils libproj-dev gdal-bin
