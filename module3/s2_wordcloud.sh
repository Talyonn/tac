#!/usr/bin/env bash

# Building a wordcloud based on one year of bulletins

YEAR=1956
cat data/*_${YEAR}_*.txt > module3/${YEAR}.txt
python module3/filtering.py $YEAR
wordcloud_cli --text module3/1956_keywords.txt --imagefile module3/1956.png --width 2000 --height 1000
display module3/${YEAR}.png