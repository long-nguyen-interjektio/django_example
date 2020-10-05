#!/bin/bash

set -e

CURRENT_UID="$( id -u)"
CURRENT_GID="$( id -g)"
#POSTGRES_ZIP_PATH="${PWD}/build/postgres:12.0-alpine.tar.gz"
#SENSDB_ZIP_PATH="${PWD}/build/sensdb-container:latest.tar.gz"

echo "${CURRENT_UID}:${CURRENT_GID}"

docker build postgresdb -t postgres:12.0-alpine
docker build . -t sensdb-container:latest

#if [ -f "$POSTGRES_ZIP_PATH" ] && [ -f "$SENSDB_ZIP_PATH" ]
#then
#    echo "$POSTGRES_ZIP_PATH and $SENSDB_ZIP_PATH exists."
#else
#  docker save postgres:12.0-alpine | gzip > "$POSTGRES_ZIP_PATH"
#  docker save sensdb-container:latest | gzip > "$SENSDB_ZIP_PATH"
#fi

export CURRENT_UID
export CURRENT_GID

docker-compose down
CURRENT_UID=${CURRENT_UID} CURRENT_GID=${CURRENT_GID} docker-compose up

