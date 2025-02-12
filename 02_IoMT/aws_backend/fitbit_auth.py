import requests
import argparse
import sys

def get_token():
    url="https://api.fitbit.com/oauth2/token"

    headers={
        "Authorization": "Basic [base64 client_id:client_secret]]",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data={
        "grant_type":"authorization_code",
        "redirect_uri":"https://localhost:8080/",
        "code":"[you code]",
        "code_verifier":"your code verifier"
    }

    response=requests.post(url,headers=headers,data=data)

    print(response.json())

def refresh_token(rf_token):
    url="https://api.fitbit.com/oauth2/token"

    headers={
        "Authorization": "Basic [base64 client_id:client_secret]]",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data={
        "grant_type":"refresh_token",
        "refresh_token":rf_token,
        "client_id":"[your client_id]"
    }

    response=requests.post(url,headers=headers,data=data)

    print(response.json())

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

    test_func = args.test_func

    if(test_func == 1):
        rf_token = "refresh token here"
        refresh_token(rf_token)
    else:
        get_token()