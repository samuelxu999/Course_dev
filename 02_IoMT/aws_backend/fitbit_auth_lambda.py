import json
import requests
import sys
import boto3

def lambda_handler(event, context):
    url="https://api.fitbit.com/oauth2/token"

    # Parse access token from event
    auth_code = event['authorization_code']

    headers={
        "Authorization": "Basic [base64 client_id:client_secret]]",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data={
        "grant_type":"authorization_code",
        "redirect_uri":"https://localhost:8080/",
        "code":auth_code
    }

    response=requests.post(url,headers=headers,data=data)

    # If the request was successfully executed, return heart rate data 
    if(response.status_code == 200):
        ret_auth = response.json()
        # create dynamodb object instance
        mydb = boto3.resource('dynamodb') 
        # new a table object given a table name 
        mytable = mydb.Table('fitbitToken') 

        # build data items from response
        item = {
            'access_token': ret_auth['access_token'],
            'refresh_token': ret_auth['refresh_token'],
            'user_id': ret_auth['user_id'],
            'expires_in': ret_auth['expires_in'],
            'token_type': ret_auth['token_type']
        }

        # save access token information to database
        mytable.put_item(Item=item)

        # return client with correct code.
        return {
            'statusCode': 200,
            # 'body': json.dumps(ret_auth)
            'body': f"Successfully get access token for user id:{ret_auth['user_id']}."
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Could not complete request for access token.'
        }
