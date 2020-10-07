#!/bin/bash
# docker_entrypoint.sh

set -e

CURRENT_UID="$( id -u)"
CURRENT_GID="$( id -g)"

echo "DOCKER_ENTRYPOINT:"
echo "$CURRENT_UID:$CURRENT_GID"

source venv/bin/activate && cd "mysite" && python manage.py test

#virtualenv --python=python2 venv
#source venv/bin/activate && pip install psycopg2-binary && python -m pip install pip-tools && pip install -r requirements.txt
#echo "INSTALLED DEPENDENCIES SUCCESSFULLY"
#chown -R "$CURRENT_UID:$CURRENT_GID" /src/django_example/.
