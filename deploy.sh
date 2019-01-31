#!/bin/bash -xe
VERSION=$(hg id -i | sed 's/+//')
TAG="navlanding:${VERSION}"

# Build new image
docker build -t "${TAG}" .
docker tag -f "${TAG}" "navlanding:latest"

# Rename running container and stop it
docker rename navlanding navlandingold
docker stop navlandingold

# Start new container
docker run -d --link pg93:postgres -p 8888:8000 --restart=on-failure:5 --name navlanding navlanding:latest

# Delete old container
docker rm navlandingold
