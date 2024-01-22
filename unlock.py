import json

import boto3
import urllib.request


def lambda_handler(event, context):
    ssm_client = boto3.client('ssm', region_name='ap-south-1')
    
    params={"commands":["usermod -U ops"],"workingDirectory":["/tmp"],"executionTimeout":["3600"]}
    
    response = ssm_client.send_command(DocumentName="AWS-RunShellScript", InstanceIds=["i-0ffeeeebe16682943"],Comment='logging the', TimeoutSeconds=600, Parameters=params)
    
    print(response)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('User Unlocked !')
    }
