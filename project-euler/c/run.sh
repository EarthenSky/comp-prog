#!/bin/bash
extension="${1##*.}"
filename="${1%.*}"
gcc $1 -Wall -lm -O3 -o $filename.out
time ./$filename.out