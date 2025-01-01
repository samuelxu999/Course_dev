import json
import requests
import argparse
import sys

def query_profile(_access_token):

    FIIBIT_API_URL = 'https://api.fitbit.com/1/user/-/profile.json'

    headers = {'Authorization': 'Bearer ' + _access_token}

    response = requests.get(FIIBIT_API_URL, headers=headers)

    if(response.status_code == 200):
        _data = response.json()

        return {
            'statusCode': 200,
            'data': _data
        }
    else:
        return {
            'statusCode': response.status_code,
            'data': 'Could not fetch profile data'
        }

def query_heartRate(_access_token):

    FIIBIT_API_URL = 'https://api.fitbit.com/1/user/-/activities/heart/date/today/today/1min.json'

    headers = {'Authorization': 'Bearer ' + _access_token}

    response = requests.get(FIIBIT_API_URL, headers=headers)

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

def gateway_HelloWorld():

    gateway_URL = "https://76zlh8kr8d.execute-api.us-east-2.amazonaws.com/test/Test"

    headers = {'Content-Type': 'application/json'}

    data = {
        'payload': 'This is a test message from sender.'
    }

    response = requests.post(gateway_URL, headers=headers, data=json.dumps(data))

    if(response.status_code == 200):
        _data = response.json()

        return {
            'statusCode': 200,
            'data': _data
        }
    else:
        return {
            'statusCode': response.status_code,
            'data': 'Could not fetch hellow world data'
        }

def gateway_heartRate(access_token):

    gateway_URL = "https://9xgokmzozd.execute-api.us-east-2.amazonaws.com/test/getHeartRate"

    headers = {'Content-Type': 'application/json'}

    data = {
        'access_token': access_token
    }

    response = requests.post(gateway_URL, headers=headers, data=json.dumps(data))

    # return response

    if(response.status_code == 200):
        # heart_rate_data = response.json()['activities-heart']

        # return {
        #     'statusCode': 200,
        #     'body': json.dumps(heart_rate_data)
        # }
        return response.json()
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Could not fetch heart data'
        }

def define_and_get_arguments(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(
		description="Run test Fitbit API client."
	)
	parser.add_argument("--test_func", type=int, default=0, help="test function option.")

	args = parser.parse_args(args=args)
	return args

if __name__ == '__main__':
    ## get arguments
    args = define_and_get_arguments()
        
    ## need manual update access token after expired time
    access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BYSjYiLCJzdWIiOiJCTjRXTUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJlY2cgcnNldCByaXJuIHJveHkgcm51dCBycHJvIHJzbGUgcmNmIHJhY3QgcmxvYyBycmVzIHJ3ZWkgcmhyIHJ0ZW0iLCJleHAiOjE3MzU3NzQwODIsImlhdCI6MTczNTc0NTI4Mn0.QCQgxwdPHfy9fbOsZ5X-1JKVnP-kzDX5euBv3SiNEhw'

    ##
    ret_data =""
    test_func = args.test_func

    if(test_func == 1):
        ret_data = query_heartRate(access_token)
    elif (test_func == 2):        
        ret_data = gateway_heartRate(access_token)
    elif (test_func == 3):     
        ret_data = gateway_HelloWorld()
    else:
        ret_data = query_profile(access_token)

    print(ret_data)

    # {"access_token":"eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BYSjYiLCJzdWIiOiJCTjRXTUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJlY2cgcnNldCByaXJuIHJveHkgcm51dCBycHJvIHJzbGUgcmNmIHJhY3QgcmxvYyBycmVzIHJ3ZWkgcmhyIHJ0ZW0iLCJleHAiOjE3MzU3NzQwODIsImlhdCI6MTczNTc0NTI4Mn0.QCQgxwdPHfy9fbOsZ5X-1JKVnP-kzDX5euBv3SiNEhw"}
