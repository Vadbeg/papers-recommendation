#!/bin/sh

docker build \
  --network host \
  -t papers_rec:1.0 \
  .
