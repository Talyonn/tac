#!/usr/bin/env bash

# Converting PDFs to text files and moving them to a new directory

for file in data/pdf/*.pdf; do pdftotext -enc UTF-8 "$file" "${file%.*}.txt"; done
mkdir data/hopitaux
mv data/pdf/*.txt data/txt/
ls data/vote | wc -l
cat data/hopitaux/all/*.txt > data/hopitaux/allvSH.txt
wc data/hopitaux/allvSH.txt
