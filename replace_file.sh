#!/bin/bash

for i in $(seq 7 25)
do
    rm "Day$i/main.py"
    cp Day6/main.py "Day$i/main.py"
done