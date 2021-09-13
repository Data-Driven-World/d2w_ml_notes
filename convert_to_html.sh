#!/bin/bash
mkdir -p output
for FILE in *; do
if [[ $FILE == *.ipynb ]]; then
    echo $FILE;
    python3 -m jupyter nbconvert $FILE --to html --output-dir ./output
    python3 convert_to_pdf.py
fi
done
