#!/bin/bash
for filename in sentiment_results_backup/*.json; do
    echo $filename
    python jsonlToCsv.py $filename
done
