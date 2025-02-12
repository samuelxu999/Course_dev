import requests
import argparse
import sys

def get_token():
    url="https://api.fitbit.com/oauth2/token"

    headers={
        "Authorization": "Basic MjNQWEo2OjllMTc3NTk3ZTA0NzdhMzBlMGRhNzdmZjIxMGEzM2E0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data={
        "grant_type":"authorization_code",
        "redirect_uri":"https://localhost:8080/",
        "code":"a56f7f2a0700d531ff84c2c8ed1829b21b34ef6a",
        "code_verifier":"511u724e18593a264u6c6i136y2q0u2d6i3o0s024x0y6l3y4u3v3v4q3u0k3f2q3d2s6a472u512m4b6v346n0c410m3j2i66025z4s4i4k3i0r5r1t13664m1q2j44"
    }

    response=requests.post(url,headers=headers,data=data)

    print(response.json())

def refresh_token(rf_token):
    url="https://api.fitbit.com/oauth2/token"

    headers={
        "Authorization": "Basic MjNQWEo2OjllMTc3NTk3ZTA0NzdhMzBlMGRhNzdmZjIxMGEzM2E0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data={
        "grant_type":"refresh_token",
        "refresh_token":rf_token,
        "client_id":"23PXJ6"
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
        rf_token = "fb5d96605a65dfe941f64e4a5e7742bee982e0f7c8dbba7eec431f5dcf4c15a4"
        refresh_token(rf_token)
    else:
        get_token()