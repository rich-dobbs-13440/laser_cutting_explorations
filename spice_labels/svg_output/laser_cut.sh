#!/bin/bash

# Check if an argument was provided
if [ $# -eq 0 ]; then
  echo "Please provide a filename as an argument."
  exit 1
fi
set -x

filename=$1

# Check if the file exists
if [ ! -f "$filename" ]; then
  echo "File '$filename' does not exist."
  exit 1
fi

# Extract the directory path and filename from the argument
directory=$(dirname "$1")
filename=$(basename "$1")

cut_file="${filename%.*}_cut.svg"
cut_filepath="$directory/$cut_file"
openscad -o "$cut_filepath" -D mode=\"Cut\" "$filename"

score_file="${filename%.*}_score.svg"
score_filepath="$directory/$score_file"
openscad -o "$score_filepath" -D mode=\"Score\" "$filename"

light_etch_file="${filename%.*}_light_etch.svg"
light_etch_filepath="$directory/$light_etch_file"
openscad -o "$light_etch_filepath" -D mode=\"Light\" "$filename"

medium_etch_file="${filename%.*}_medium_etch.svg"
medium_etch_filepath="$directory/$medium_etch_file"
openscad -o "$medium_etch_filepath" -D mode=\"Medium\" "$filename"

heavy_etch_file="${filename%.*}_heavy_etch.svg"
heavy_etch_filepath="$directory/$heavy_etch_file"
openscad -o "$heavy_etch_filepath" -D mode=\"Heavy\" "$filename"

