#!/bin/bash

# Define the service details
service_name="example.com"
service_port=80

# Monitor the service availability
while true
do
    response_code=$(curl -sL -w "%{http_code}" "http://$service_name:$service_port" -o /dev/null)
    if [[ $response_code == 200 ]]; then
        echo "$(date +"%Y-%m-%d %H:%M:%S") - Service $service_name is UP"
    else
        echo "$(date +"%Y-%m-%d %H:%M:%S") - Service $service_name is DOWN"
    fi
    sleep 10
done
