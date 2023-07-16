# AWS CloudFormation Template: Test & Production Environment Setup

This AWS CloudFormation template aims to set up a comprehensive development environment, including test and production environments, for a project that involves transferring large files through AWS. The project requires better storage and bandwidth management, data integrity, and cost optimization. The primary technologies utilized in the development are Laravel, Python, and Node.js.

## Prerequisites

Before deploying this CloudFormation template, ensure that you have the following:

1. AWS account with appropriate permissions to create resources.
2. Familiarity with AWS CloudFormation and its deployment process.

## Template Overview

This CloudFormation template includes the following resources and configurations:

1. Two Virtual Private Clouds (VPCs):
   - Test VPC with a public subnet for test environment.
   - Production VPC with a public subnet for production environment.

2. Internet Gateways:
   - Internet gateways are attached to both VPCs to enable internet connectivity.

3. Security Groups:
   - Separate security groups are created for test and production instances to control inbound and outbound traffic.

4. IAM Roles and Instance Profiles:
   - IAM roles are created for various user roles setup, such as Master Admin, Senior Developer, Junior Developer, Main Server Administrator, and Junior Server Administrator.
   - An IAM role is also created for instance automation.

5. EC2 Instance for Development:
   - A t2.micro EC2 instance is provisioned for development purposes. Developers can push code to this instance using SSH connections.

6. S3 Bucket for Large File Storage:
   - An S3 bucket is created to store large files (50-100 GB) in a folder structure. This bucket allows private access for better data integrity and verification at the download end.

## Usage

1. **Deploy the CloudFormation Stack**: Use the AWS Management Console or AWS CLI to deploy this CloudFormation template. Provide the required parameters during the deployment process, such as the name of the SSH key pair for the development instance.

2. **Access Development Instance**: Once the stack is deployed successfully, you can access the development instance using the provided SSH key pair.

3. **Large File Storage**: The S3 bucket created by this template will be available for storing large files in a folder structure. Ensure to manage access controls and data integrity appropriately.

4. **User Role Setup**: The template creates IAM roles for different user roles. Assign these roles to respective team members based on their responsibilities.

5. **Instance Automation**: Utilize the IAM role for instance automation wherever required to streamline your infrastructure management.

## Customization

You can customize this CloudFormation template to fit your specific project requirements:

1. Adjust instance types, subnets, security groups, and IAM roles as needed.

2. Modify access controls for the S3 bucket and other resources based on your security policies.

3. Extend the template to include other resources like load balancers, NAT gateways, etc.

## Note

1. Ensure you carefully review and understand the resources created by this CloudFormation template before deployment.

2. Always test the CloudFormation stack in a controlled environment before deploying to production to avoid any unexpected issues.

3. This template provides a basic setup for development, and you may need to add further resources and configurations to meet your specific use case.

4. Regularly monitor and optimize your AWS resources to achieve cost optimization and better performance.

For any questions or assistance, contact your AWS administrator or AWS support.

---

## Revision History

- Version 1.0 (Initial Release) - [16/07/2023]
  - Basic CloudFormation template with VPCs, Subnets, Internet Gateways, Security Groups, IAM Roles, and EC2 Instance for development.
- Version 1.1 - [16/07/2023]
  - Added S3 bucket for large file storage and improved IAM roles for better user role setup.
- Version 1.2 - [16/07/2023]
  - Updated the CloudFormation template to address specific security and networking requirements.
- Version 2.0 - [16/07/2023]
  - Comprehensive CloudFormation template with additional features for cost optimization and data integrity.

## License

This CloudFormation template is released under the [MIT License](LICENSE).

## Contributors

- [Charles Mwaniki](https://github.com/mwanikigachanja) - [https://charlesmwaniki.co.ke]

## Acknowledgments

Special thanks to the AWS team and contributors for their invaluable work and support.

If you have any feedback or suggestions, please feel free to submit an issue or a pull request. We welcome your contributions to improve this CloudFormation template for the community.
