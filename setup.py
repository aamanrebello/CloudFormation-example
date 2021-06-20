import boto3

#This function creates the template defined in tmpl.json on being called.
#
#   - private_key_name is the name of the private-public key pair that
#     you are going to use.
#   - template_url is the url of the JSON file defining the cloudFormation
#     stack, which is stored in S3.
#   - stack_name is the name that you want to give the infrastructure stack
#     that is allocated.

def createtmpl(private_key_name, template_url, stack_name='Mystack'):
    client = boto3.client('cloudformation')

    response = client.create_stack(
        StackName = stack_name,
        TemplateURL = template_url,
        Parameters=[
            {
                'ParameterKey': 'KeyName',
                'ParameterValue': private_key_name
            }
        ],
        ResourceTypes=[
            'AWS::EC2::Instance',
            'AWS::EC2::SecurityGroup'
        ],
        OnFailure='ROLLBACK',
        EnableTerminationProtection=False
    )

    print(response)

#------------------------------------------------------------------------
#Example function call

createtmpl(
   private_key_name = 'keytime',
   template_url = 'https://cf-templates-tqabeo4q9oey-us-east-1.s3.amazonaws.com/20201985qe-tmpl.json'
)
#------------------------------------------------------------------------
