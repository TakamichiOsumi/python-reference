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
    cp ./../snippets.py A.py
    touch A_{1..3}.txt
    cp ./../snippets.py B.py
    touch B_{1..3}.txt
    cp ./../snippets.py C.py
    touch C_{1..3}.txt
    cp ./../snippets.py D.py
    touch D_{1..3}.txt
    cp ./../snippets.py E.py
    touch E_{1..3}.txt
    echo "Created a new directory"
fi
