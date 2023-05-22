#!/bin/zsh

for file in $PWD/*.ipynb; do 
    echo $file
    jupyter nbconvert  --to markdown $file; 
done