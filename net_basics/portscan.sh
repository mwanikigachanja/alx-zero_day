#!/bin/bash

# Define the target host and range of ports
target_host="example.com"
start_port=1
end_port=100

# Perform the port scan
for (( port=$start_port; port<=$end_port; port++ ))
do
    (echo >/dev/tcp/$target_host/$port) >/dev/null 2>&1 && echo "Port $port is open"
done

# Example output: Port 22 is open
# Example output: Port 80 is open
# Example output: ...

