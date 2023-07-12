#!/bin/bash

# Define the domain name
domain="example.com"

# Perform the IP address lookup
ip_address=$(nslookup $domain | grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}")

echo "IP Address: $ip_address"

# Example output: IP Address: 93.184.216.34

