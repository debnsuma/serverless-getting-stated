import simplejson as json
import boto3
import os 
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')

def lambda_handler(event, context):
    
    table = dynamodb.Table(table_name)
    
    # Read the order ID 
    order_id = int(event["pathParameters"]["id"])
    
    # Query the table with the key 
    response = table.query(KeyConditionExpression=Key("id").eq(order_id))
    print(response)
    
    return {
        'statusCode' : 200,
        'headers' : {},
        'body' : json.dumps(response['Items'])
    }
        