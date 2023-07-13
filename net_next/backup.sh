#!/bin/bash

# Define source and destination directories
source_dir="/path/to/source"
destination_dir="/path/to/backup"

# Create a timestamp for the backup filename
timestamp=$(date +"%Y%m%d%H%M%S")

# Create a backup directory with the current timestamp
backup_dir="$destination_dir/backup_$timestamp"
mkdir -p $backup_dir

# Copy the files from the source directory to the backup directory
cp -R $source_dir $backup_dir

# Example output: [Copying files...]

echo "Backup completed successfully."
