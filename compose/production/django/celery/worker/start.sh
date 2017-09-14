#!/bin sh

set -o errexit
set -o pipefail
set -o nounset

python entrypoint.py
celery -A apps.tasks worker -l INFO
