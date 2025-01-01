import json
import requests


FIIBIT_API_URL = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/today/1min.json'

def lambda_handler(event, context):
    # TODO implement

    # Parse access token from event
    _access_token = event['access_token']

    # Set headers
    headers = {'Authorization': 'Bearer ' + _access_token}

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