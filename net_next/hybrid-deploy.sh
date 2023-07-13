#!/bin/bash

# Define the deployment configuration
app_name="my_app"
on_premises_servers=("on_premises_server1" "on_premises_server2")
cloud_servers=("cloud_server1" "cloud_server2")
deploy_dir="/path/to/deployment"

# Deploy to on-premises servers
for server in "${on_premises_servers[@]}"
do
    scp -r $deploy_dir $server:/opt/$app_name
    ssh $server "sudo systemctl restart $app_name"
done

# Deploy to cloud servers
for server in "${cloud_servers[@]}"
do
    scp -r $deploy_dir $server:/opt/$app_name
    ssh $server "sudo systemctl restart $app_name"
done

echo "Application deployed successfully."
