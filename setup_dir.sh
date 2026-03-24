#!/bin/bash

if [ X${1} = "X" ]; then
    echo "Input the name of directory"
    exit 1
else
    mkdir $1
    cd $1
    cp ../template.py A.py
    cp ../template.py B.py
    cp ../template.py C.py
    cp ../template.py D.py
    cp ../template.py E.py
fi
