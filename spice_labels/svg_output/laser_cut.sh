#!/bin/bash

# Check if an argument was provided
if [ $# -eq 0 ]; then
  echo "Please provide a filename as an argument."
  exit 1
fi


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
cut_filepath="$directory/$new_filename"

openscad -o '$filename' -D mode=Cut '$filename'