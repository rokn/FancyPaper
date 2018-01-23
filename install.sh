#!/bin/sh

MAIN="src/main.py"

chmod +x $MAIN

dir=$(pwd)

cd /bin/

ln -s "$dir/$MAIN" fancypaper


