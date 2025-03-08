import json
import requests
import sys
from datetime import datetime, timedelta
import boto3

def get_fitbit_auth():
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
    return GetItem['Item']

def lambda_handler(event, context):
    ## retrive fitbit authorization data from db
    fitbit_auth = get_fitbit_auth()

    ## set access token and refresh token
    access_token = fitbit_auth['access_token']['S']
    refresh_token = fitbit_auth['refresh_token']['S']
    time_stamp = fitbit_auth['time_stamp']['S']
    expires_in = fitbit_auth['expires_in']['N']

    ## convert time stamp to time object
    datetime_object = datetime.strptime(time_stamp, "%Y-%m-%d %H:%M:%S")
    ## add expired seconds to check if token is expired
    datetime_offset = datetime_object + timedelta(seconds=int(expires_in))
    
    ## check if token has been expired
    if(datetime_offset<datetime.now()):
        print("Access token has expired. Not refresh token. Need a new token authorization.")
    else:
        ## update token if token is still valid

        ## set refresh url
        url="https://api.fitbit.com/oauth2/token"

        headers={
            "Authorization": "Basic [base64 client_id:client_secret]]",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data={
            "grant_type":"refresh_token",
            "refresh_token":refresh_token,
            "client_id":"[Client ID]"
        }

        ## send refresh token request.
        response=requests.post(url,headers=headers,data=data)

        # If the request was successfully executed, put new authrization data to Table-fitbitToken 
        if(response.status_code == 200):
            ret_auth = response.json()
            # create dynamodb object instance
            mydb = boto3.resource('dynamodb') 
            # new a table object given a table name 
            mytable = mydb.Table('fitbitToken')

            # Get current date and time
            now = datetime.now()
            # Format the output of timesamp
            formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

            # build data items from response
            item = {
                'access_token': ret_auth['access_token'],
                'refresh_token': ret_auth['refresh_token'],
                'user_id': ret_auth['user_id'],
                'expires_in': ret_auth['expires_in'],
                'token_type': ret_auth['token_type'],
                'time_stamp': formatted_date_time
            }

            # save access token information to database
            mytable.put_item(Item=item)

            # return client with correct code.
            json_return = {
                'statusCode': 200,
                # 'body': json.dumps(ret_auth)
                'body': f"Successfully refreshed access token for user id:{ret_auth['user_id']}."
            }
            print(json_return)
        else:
            json_return = {
                'statusCode': response.status_code,
                'body': 'Could not complete request for access token.'
            }
            print(json_return)
