#!/bin/sh

docker run \
  -p 8080:8080 \
  -e PAPERS_WITH_CODE_TOKEN_ENV=$1 \
  -v "$(pwd)"/models:/app/models \
  papers_rec:1.0
