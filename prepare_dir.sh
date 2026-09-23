#!/bin/bash

if [ X${1} = "X" ]; then
    echo "Input the name of directory"
    exit 1
else
    if [ -d ${1} ]; then
	echo "The directory already exists"
	exit 1
    fi
    mkdir $1
    cd $1
    # Prepare some files in advance.
    for c in `echo "A B C D E F G"`
    do
	cp ./../snippets.py ./$c.py
    done
    echo "Created a new directory"
fi
