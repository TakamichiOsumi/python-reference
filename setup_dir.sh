#!/bin/bash

if [ X${1} = "X" ]; then
    echo "Input the name of directory"
    exit 1
else
    mkdir $1
    cd $1
    cp ../template.py A.py
    touch A_{1..3}.txt
    cp ../template.py B.py
    touch B_{1..3}.txt
    cp ../template.py C.py
    touch C_{1..3}.txt
    cp ../template.py D.py
    touch D_{1..3}.txt
    cp ../template.py E.py
    touch E_{1..3}.txt
fi
