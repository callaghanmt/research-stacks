#!/bin/bash
# Build a docker image from a file or several fragments

mkdir -p dockertest
# Make an empty file
echo "" > dockertest/Dockerfile

for var in "$@"
do
	echo "Adding $var to recipe"
	cat "$var" >> dockertest/Dockerfile
done

docker build dockertest -t research-stacks/dockertest


