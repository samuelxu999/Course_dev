import json
import requests
import boto3

# load access token data from database
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

def save_heart_rate_data(heart_rate_json):
    # create dynamodb object instance
    mydb = boto3.resource('dynamodb') 
    # new a table object given a table name 
    mytable = mydb.Table('HeartRate')

    # put item into the table
    mytable.put_item(
        Item={
            'collect_date': heart_rate_json['dateTime'],
            'restingHeartRate': heart_rate_json['value']['restingHeartRate'],
            'heartRateZones': json.dumps(heart_rate_json['value']['heartRateZones'])
        }
    )

def lambda_handler(event, context):
    # TODO implement

    _access_token = get_access_token()
    _collectdate = event['collect_date']

    # Set headers
    headers = {'Authorization': 'Bearer ' + _access_token}

    # Set API URL
    FIIBIT_API_URL = 'https://api.fitbit.com/1/user/-/activities/heart/date/'+ _collectdate + '/1d.json'

    # make request [GET] to Fitbit API
    response = requests.get(FIIBIT_API_URL, headers=headers)

    # If the request was successfully executed, return heart rate data 
    if(response.status_code == 200):
        heart_rate_data = response.json()['activities-heart'][0]

        # save 1d heart rate data to database
        save_heart_rate_data(heart_rate_data)
        
        return {
            'statusCode': 200,
            'body': 'Successfully collected heart rate data and save to database.'
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Could not collect heart rate data and save to database.'
        }