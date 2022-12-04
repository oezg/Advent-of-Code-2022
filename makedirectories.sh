#!/bin/bash

for i in $(seq 6 25)
do
    mkdir "Day$i"
    cp Day5/input.txt "Day$i/input.txt"
    cp Day5/README.md "Day$i/README.md"
    cp Day5/main.py "Day$i/main.py"
done