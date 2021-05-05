import json
import os 
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    
    topic = os.environ['PATIENT_CHECKOUT_TOPIC']

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
        sns.publish(
            TopicArn = topic,
            Message = json.dumps({"default" : json.dumps(each_event)}),
            MessageStructure = 'json'
        )
        