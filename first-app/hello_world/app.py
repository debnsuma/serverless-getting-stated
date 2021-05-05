import json
import time
import os 
import random 

global_random_val = random.random()
def cold_start_basics(event, context):
    local_val = random.random()
    print(local_val)
    print(global_random_val)

def first_lambda(event, context):

    return f"Hello {event}" 

def foo(event, context):
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    time.sleep(1) 
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())
    
    print(os.getenv('restapiurl'))
    return event
