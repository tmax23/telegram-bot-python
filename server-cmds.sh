#!/usr/bin/env bash

export IMAGE=$1
export TOKEN=$2
export PUBLIC_IP=$3
docker-compose -f docker-compose.yaml down
docker pull $1
docker-compose -f docker-compose.yaml up --detach
