# CloudFormation VPC and EC2 Instances

This CloudFormation template creates a Virtual Private Cloud (VPC) along with EC2 instances, including a Bastion Host, Web Server, App Server, and a Relational Database Service (RDS) instance. The infrastructure is designed to be highly available by utilizing multiple availability zones and securely connected through security groups.

## Prerequisites

Before using this CloudFormation template, ensure you have the following:

1. An AWS account with sufficient permissions to create VPC, EC2 instances, RDS instance, and related resources.
2. A valid EC2 key pair for SSH access to the instances.

## How to Use

1. Clone this repository to your local machine or download the CloudFormation template directly from the provided link.
2. Navigate to the AWS CloudFormation console: https://console.aws.amazon.com/cloudformation
3. Click "Create Stack."
4. Choose "Upload a template file," and then click "Choose file" to upload the `cloudformation-template.yaml` file from your local machine.
5. Click "Next."
6. Provide a stack name, and then fill in the required parameters, such as VPC CIDR, public and private subnets CIDRs, etc.
7. Click "Next."
8. Optionally, you can add tags for your stack. Tags are useful for organizing resources.
9. Click "Next."
10. Review the stack settings, and if everything looks good, click "Create stack."

AWS CloudFormation will now start provisioning the specified resources based on the template.

## Outputs

Once the stack creation is complete, the following outputs will be available in the CloudFormation stack:

- **VPCID**: The ID of the created Virtual Private Cloud.
- **PublicSubnetID**: The ID of the public subnet.
- **PrivateSubnet1ID**: The ID of the first private subnet.
- **PrivateSubnet2ID**: The ID of the second private subnet.
- **PrivateSubnet3ID**: The ID of the third private subnet.
- **BastionHostIP**: The public IP address of the Bastion Host.
- **WebServerIP**: The public IP address of the Web Server.
- **AppServerIP**: The public IP address of the App Server.
- **DBEndpoint**: The endpoint of the RDS Database.

You can use these outputs to access the created instances and resources.

## SSH Access to Instances

To access the instances created by this template, use the provided key pair and the public IP addresses obtained from the outputs.

Example command to SSH into the Bastion Host:

```
ssh -i /path/to/your/keypair.pem ec2-user@BastionHostIP
```

Replace `/path/to/your/keypair.pem` with the actual path to your private key file and `BastionHostIP` with the public IP address of the Bastion Host.

## Cleanup

To delete the entire stack and associated resources:

1. Navigate to the AWS CloudFormation console: https://console.aws.amazon.com/cloudformation
2. Select the stack you created with this template.
3. Click "Delete."
4. Confirm the deletion when prompted.

Please note that deleting the stack will terminate all the instances and associated resources, including the RDS database. Make sure to back up any important data before deleting the stack.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

The CloudFormation template provided in this project deploys AWS resources. By default, it may incur costs for using these services. It is the user's responsibility to review and understand the associated costs and manage the resources accordingly. The author of this project is not responsible for any unexpected charges or damages incurred during the use of this template.

## Contributions

Contributions to improve the template or add new features are welcome! Please create a pull request with your proposed changes.

If you encounter any issues or have suggestions for improvement, please feel free to open an issue.
