#!/bin/bash

# Define the network interface to monitor
network_interface="eth0"

# Capture network traffic to a file
tcpdump -i $network_interface -w network_traffic.pcap

# Analyze network traffic using tshark
tshark -r network_traffic.pcap -q -z io,stat,100,"COUNT(frame) frame" -q -z conv,tcp

# Example output: [Network traffic statistics and TCP conversations]

echo "Network traffic analysis completed."
