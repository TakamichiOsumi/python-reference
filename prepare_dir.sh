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
    # Copy utility scripts.
    cp ./../pbcopy_latest.sh ./
    cp ./../execute_latest.sh ./
    cp ./../debug_latest.sh ./
    echo "Created a new directory"
fi
