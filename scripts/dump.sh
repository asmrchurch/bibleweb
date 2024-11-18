#!/bin/bash

# Output file
OUTPUT_FILE="all_js_files_combined.js"

# Clear the output file if it already exists
> "$OUTPUT_FILE"

# Loop through all JavaScript files tracked by git
git ls-files '*.js' | while read -r file; do
  echo "// File: $file" >> "$OUTPUT_FILE"
  cat "$file" >> "$OUTPUT_FILE"
  echo -e "\n\n" >> "$OUTPUT_FILE" # Add spacing between files
done

echo "All JavaScript files have been concatenated into $OUTPUT_FILE"

