#!/bin sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python entrypoint.py
/usr/local/bin/gunicorn conf.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app