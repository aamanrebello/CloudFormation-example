# CloudFormation-example

A small example of using AWS CloudFormation to set up an EC2 instance in a private network (VPC).

## Prerequisites

1. You need to have an AWS account set up.
2. The AWS SDK for Python Boto3 needs to be installed. This can be done from the [repo](https://github.com/boto/boto3) or via a software like pip.
3. The above SDK needs to be configured to your AWS account credentials (instructions in the [repo](https://github.com/boto/boto3) README).

## How to Use

1. (*tmpl.json*)[tmpl.json] describes the configuration of the EC2 instance. It must be stored in an AWS S3 bucket as an object - you need the URL of this object. 
2. A public-private key pair needs to be created. Information [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html). You need the name of this key pair.
3. Using the URL from 1 and the key pair name from 2, you can use the function from (*setup.py*)[setup.py]. See the example function call in that file.
4. Feel free to modify *tmpl.json* to modify or add more features to your CloudFormation stack. 
