#!/bin/bash
# Build a docker image from a file or several fragments
# Pass docker image name followed by Dockerfile or ordered fragments
mkdir -p $1
# Make an empty file
echo "" > $1/Dockerfile

for var in "$@"
do
	if [ "$1" != "$var" ]
	then
		echo "Adding $var to recipe"
		cat "$var" >> ${1}/Dockerfile
	fi
done

docker build $1 -t research-stacks/$1


