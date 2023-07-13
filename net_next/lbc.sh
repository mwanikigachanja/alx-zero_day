#!/bin/bash

# Define the load balancer IP and backend servers
load_balancer_ip="load_balancer_ip"
backend_servers=("backend_server1" "backend_server2" "backend_server3")

# Configure the load balancer
for server in "${backend_servers[@]}"
do
    iptables -A FORWARD -p tcp --dport 80 -d $server -j ACCEPT
done

iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination $load_balancer_ip
iptables -t nat -A POSTROUTING -j MASQUERADE

echo "Load balancer configuration applied successfully."

