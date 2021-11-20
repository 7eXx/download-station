#!/bin/bash

# exporting all variables importing
set -o allexport
[ -z .env ] && source .env
[ -z .env.local ] && source .env.local
set +o allexport

# set command printing and errors
set -xe

# start docker compose with all the services
docker-compose --file=./docker-compose.yml up -d
