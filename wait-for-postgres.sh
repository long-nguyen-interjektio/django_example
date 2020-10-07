#!/bin/bash
# wait-for-postgres.sh

set -e

CMD="$1"
POSTGRES_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${DB_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
SKIP_DB_SETUP=false

echo "cmd: $CMD"
echo "${POSTGRES_PASSWORD}"
echo "${POSTGRES_USER}"
echo "${POSTGRES_DB}"
echo "${DB_HOST}"
echo "${POSTGRES_PORT}"

POSTGRESQL_INIT_FAIL=true

for i in {1..200}
do
  psql "${POSTGRES_URL}" -c '\q' 2>/dev/null 1>/dev/null && POSTGRESQL_INIT_FAIL=false && break
  echo "Attemting to connect to Postgres - sleeping ${i}"
  sleep 1
done

$POSTGRESQL_INIT_FAIL && echo "Postgres is unavailable" && exit 1
echo "Postgres is up - executing command: ${CMD}"
exec "$CMD"
