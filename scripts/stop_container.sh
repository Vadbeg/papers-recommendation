#!/bin/sh

docker stop $(docker ps -q --filter ancestor=papers_rec:1.0)
