#!/bin/sh

docker run \
  -p 0.0.0.0:8000:8000 \
  -e PAPERS_WITH_CODE_TOKEN_ENV=$1 \
  -v "$(pwd)"/models:/app/models \
  --ipc=host \
  -it \
  papers_rec:1.0
