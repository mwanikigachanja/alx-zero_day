#!/bin/bash

# Define the network interface to monitor
network_interface="eth0"

# Log network statistics to a file
while true
do
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    rx_bytes=$(cat "/sys/class/net/$network_interface/statistics/rx_bytes")
    tx_bytes=$(cat "/sys/class/net/$network_interface/statistics/tx_bytes")

    echo "$timestamp RX: $rx_bytes bytes | TX: $tx_bytes bytes" >> network_stats.log

    sleep 5
done
