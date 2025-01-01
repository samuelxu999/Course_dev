import json

def lambda_handler(event, context):
    # parse payload and then return it
    payload = event['payload']
    responseBody = {
        'payload': payload,
        'message': 'Hello from Lambda Function!'
    }
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(responseBody)
    }
