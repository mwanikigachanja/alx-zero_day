#!/bin/bash

# Define source and destination files
source_file="local_file.txt"
destination_host="remote_host"
destination_directory="/path/to/destination"

# Perform the file transfer using SCP
scp $source_file $destination_host:$destination_directory

# Example output: local_file.txt 100% 0     0.0KB/s   00:00

