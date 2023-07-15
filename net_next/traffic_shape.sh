#!/bin/bash

# Define network traffic shaping rules
tc qdisc add dev eth0 root handle 1: htb default 30
tc class add dev eth0 parent 1: classid 1:1 htb rate 1000mbit
tc class add dev eth0 parent 1:1 classid 1:10 htb rate 500mbit
tc class add dev eth0 parent 1:1 classid 1:20 htb rate 300mbit
tc class add dev eth0 parent 1:1 classid 1:30 htb rate 200mbit

# Apply packet filtering and routing
tc filter add dev eth0 parent 1:0 protocol ip prio 1 u32 match ip dport 80 0xffff flowid 1:10
tc filter add dev eth0 parent 1:0 protocol ip prio 2 u32 match ip dport 22 0xffff flowid 1:20

echo "Network traffic shaping rules applied."
