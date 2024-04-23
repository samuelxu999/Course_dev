#!/usr/bin/env python

'''
========================
WS_Client module
========================
Created on Nov.2, 2017
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module provide encapsulation of client API that access to Web service.
'''
import time
import requests
import datetime
import json
import argparse
import sys


def test_query(token_id):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/query'
    data_args={}
    data_args['token_id'] = token_id

    response = requests.get(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def test_deposit(token_id, value):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/deposit'
    data_args={}
    data_args['token_id'] = token_id
    data_args['token_value'] = value

    response = requests.post(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def test_withdraw(token_id, value):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/withdraw'
    data_args={}
    data_args['token_id'] = token_id
    data_args['token_value'] = value

    response = requests.post(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response


def test_setpolicy(token_id, value):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/setpolicy'
    data_args={}
    data_args['token_id'] = token_id
    data_args['token_policy'] = value

    response = requests.post(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def test_getpolicy(token_id):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/getpolicy'
    data_args={}
    data_args['token_id'] = token_id

    response = requests.get(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def define_and_get_arguments(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Run Test client."
    )

    parser.add_argument("--test_func", type=int, default=0, 
                        help="Execute test function: 0-query, 1-deposit \
                                                    2-withdraw, 3-set_policy, 4-get_policy")

    parser.add_argument("--id", type=int, default=1, 
                        help="input token id (int)")

    parser.add_argument("--value", type=int, default=1, help="set balance value")

    parser.add_argument("--policy", type=str, default="Test policy", help="set policy string")

    args = parser.parse_args(args=args)
    return args

if __name__ == "__main__":
    args = define_and_get_arguments()

    token_id = args.id
    token_value = args.value
    token_policy = args.policy

    if(args.test_func==1): 
        recepit = test_deposit(token_id, token_value)
        print("token %d deposit has receipt %s" %(token_id, recepit))
    elif(args.test_func==2):
        recepit = test_withdraw(token_id, token_value)
        print("token %d withdraw has receipt %s" %(token_id, recepit))
    elif(args.test_func==3):
        recepit = test_setpolicy(token_id, token_policy)
        print("token %d setpolicy has receipt %s" %(token_id, recepit))
    elif(args.test_func==4):
        token_data = test_getpolicy(token_id)
        print("token %d has policy: %s" %(token_data['id'], token_data['policy']))        
    else:     
        token_data = test_query(token_id)
        # print(token_data)
        print("token %d has balance %d" %(token_data['id'], token_data['balance']))
