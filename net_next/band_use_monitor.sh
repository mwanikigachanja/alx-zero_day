#!/bin/bash

# Define the network interface to monitor
network_interface="eth0"

# Set the monitoring duration (in seconds)
monitoring_duration=3600

# Monitor bandwidth usage and generate reports
for ((i=0; i<$monitoring_duration; i+=5))
do
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    bandwidth_usage=$(ifstat -i $network_interface -T 5 1 | awk '/Total:/ {print $8}')
    echo "$timestamp,$bandwidth_usage" >> bandwidth_usage.csv
    sleep 5
done

echo "Bandwidth usage monitoring completed."
