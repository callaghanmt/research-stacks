#!/bin/bash
# Build a docker image from a file

mkdir dockertest
cp $1 dockertest/Dockerfile

docker build dockertest -t research-stacks:dockertest


