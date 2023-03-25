#!/bin/bash

# This script turns all shell scripts in a directory into executable files

# Change directory to the target directory
cd /path/to/directory

# Loop through each shell script in the directory and set the executable flag
for file in *.sh
do
  chmod +x $file
done

# Output a message indicating completion of the script
echo "All shell scripts in the directory are now executable"
