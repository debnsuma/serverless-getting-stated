import json
import boto3 

s3 = boto3.client('s3')


def lambda_handler(event, context):
    
    # Fetch Bucket details from the event 
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    # Read the data from S3 
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    data = obj['Body'].read().decode('utf-8')
    checkout_events = json.loads(data)

    # Iterate through the all the data in the 'checlout_event'
    for each_event in checkout_events:
        print(each_event)
        
        
    
    
    
    
