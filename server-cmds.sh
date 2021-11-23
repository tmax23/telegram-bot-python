#!/usr/bin/env bash

export IMAGE=$1
export PUBLIC_IP=$2
docker-compose -f docker-compose.yaml down
docker pull $1
docker-compose -f docker-compose.yaml up --detach
