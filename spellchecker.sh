#!/bin/bash

echo "Enter the folder path:"
read folder_path

if [ ! -d "$folder_path" ]; then
  echo "Folder not found!"
  exit 1
fi

for file in "$folder_path"/*; do
  if [ -f "$file" ]; then
    echo "Spell checking: $file"
    aspell check "$file"
    echo
  fi
done