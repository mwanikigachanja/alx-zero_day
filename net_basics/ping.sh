#!/bin/bash

# Define the target host
target_host="example.com"

# Perform the ping test
ping -c 4 $target_host

# Example output: PING example.com (93.184.216.34): 56 data bytes
# Example output: 64 bytes from 93.184.216.34: icmp_seq=0 ttl=57 time=26.559 ms
# Example output: ...

