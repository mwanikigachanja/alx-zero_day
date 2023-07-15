#!/bin/bash

# Define the list of network devices
devices=("192.168.0.1" "192.168.0.2" "192.168.0.3")

# Define the backup directory
backup_dir="/path/to/backup"

# Loop through the devices and backup configurations
for device in "${devices[@]}"
do
    sshpass -p "password" ssh user@$device "show running-config" > $backup_dir/$device-config.txt
done

echo "Configurations backed up successfully."

