#!/bin/bash

# Define the target host
target_host="example.com"

# Perform ping tests
ping_results=$(ping -c 10 $target_host)

# Extract statistics
packet_loss=$(echo "$ping_results" | grep -oE "[0-9]+% packet loss")
latency_stats=$(echo "$ping_results" | grep -oE "min/avg/max/mdev = [0-9.]+/[0-9.]+/[0-9.]+/[0-9.]+ ms")

echo "Ping Statistics:"
echo "----------------"
echo "$packet_loss"
echo "$latency_stats"

