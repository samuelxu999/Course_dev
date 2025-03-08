import json
import requests
import boto3

def get_access_token():
    # create dynamodb client instance
    myclient = boto3.client('dynamodb') 

    # get the item from the table
    GetItem = myclient.get_item(
        TableName='fitbitToken',
        Key={
            'user_id': {
                'S': 'BN4WML'
            },
        }
    )
    return GetItem['Item']['access_token']['S']

def lambda_handler(event, context):
    # TODO implement

    _access_token = get_access_token()
    _startdate = event['startdate']
    _enddate = event['enddate']


    # Set headers
    headers = {'Authorization': 'Bearer ' + _access_token}

    # Set API URL
    FIIBIT_API_URL = 'https://api.fitbit.com/1/user/-/activities/heart/date/'+ _startdate + '/' + _enddate + '.json'

    # make request [GET] to Fitbit API
    response = requests.get(FIIBIT_API_URL, headers=headers)

    # If the request was successfully executed, return heart rate data 
    if(response.status_code == 200):
        heart_rate_data = response.json()['activities-heart']

        return {
            'statusCode': 200,
            'body': json.dumps(heart_rate_data)
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Could not fetch heart data'
        }