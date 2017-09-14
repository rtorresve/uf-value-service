#!/bin sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python entrypoint.py
python manage.py migrate
python manage.py get_hystoric_uf_value_by_year -f 1980 -t 2017
/usr/local/bin/gunicorn conf.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app