import json
import boto3

def lambda_handler(event, context):
    print(event)
    ec2 = boto3.client('ec2')
    
    detail = event['detail']
    user_identity = detail['userIdentity']['type']
    instance_id = detail['requestParameters']['instancesSet']['items'][0]['instanceId']
    
    response = ec2.create_tags(
    Resources = 
    [
        instance_id
    ],
        Tags=[
            {
                'Key': 'Name',
                'Value': user_identity
            },
        ]
    )
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Tagging operation completed')
    }
    
    
    
