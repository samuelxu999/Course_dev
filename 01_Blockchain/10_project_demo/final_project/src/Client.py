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

def getAddress(node_name):
    address_json = json.load(open('./addr_list.json'))
    return address_json[node_name]

def test_query(hash_ref):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/query'
    data_args={}
    data_args['hash_ref'] = hash_ref

    response = requests.get(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def test_register(hash_ref, json_ref):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/register'
    data_args={}
    data_args['hash_ref'] = hash_ref
    data_args['token_value'] = json_ref

    response = requests.post(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def test_burn(hash_ref, account_id):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/burn'
    data_args={}
    data_args['hash_ref'] = hash_ref
    data_args['account_id'] = account_id

    response = requests.post(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response


def test_transfer(hash_ref, to_address):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/transfer'
    data_args={}
    data_args['hash_ref'] = hash_ref
    data_args['to_address'] = to_address

    response = requests.post(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def test_tracker(hash_ref):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Token/tracker'
    data_args={}
    data_args['hash_ref'] = hash_ref

    response = requests.get(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def test_dataupload(file_name):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Data/upload'
    data_args={}
    data_args['file_name'] = file_name

    response = requests.get(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def test_datadownload(file_name, file_cid):
    headers = {'Content-Type' : 'application/json'}

    api_url = 'http://localhost:8080/Data/downlad'
    data_args={}
    data_args['filename'] = file_name
    data_args['public'] = file_cid

    response = requests.get(api_url, data=json.dumps(data_args), headers=headers)

    json_response = response.json()      

    return json_response

def define_and_get_arguments(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Run Test client."
    )

    parser.add_argument("--test_func", type=int, default=0, 
                        help="Execute test function: 0-upload file, 1-download file \
                                                    2-check token, 3-register token, 4-burn token \
                                                    5-transfer token, 6-check tracker")
    parser.add_argument("--op", type=int, default=0, 
                        help="operation mode")

    parser.add_argument("--account_id", type=int, default=0, 
                        help="input token id (int)")

    parser.add_argument("--value", type=int, default=1, help="set balance value")

    parser.add_argument("--policy", type=str, default="Test policy", help="set policy string")

    args = parser.parse_args(args=args)
    return args

if __name__ == "__main__":
    args = define_and_get_arguments()

    account_id = args.account_id
    # account_name = args.account_name

    hash_ref = '0x5aa101f0ec62a04329d2db2e8763c55cc10ba3d7a6a08f4557aa15159ce3a7c9'
    json_ref = {}
    json_ref['file_owner'] = getAddress('account0')
    json_ref['file_name'] = "test_file.txt"
    json_ref['file_cid'] = "QmSK2tz19L38cQFZkAbSwtJ8cRXKjE8CPy73tPpFLz9DGc"
    json_ref['file_size'] = 22


    if(args.test_func==1): 
        if(args.op==1):
            file_name = 'test_figure.png'
            file_cid = 'QmUzU9hnuNiDysUj7QzWUJVSWbaFnnz8QEyM7QjvcdTN8B'
        else:
            file_name = 'test_file.txt'
            file_cid = 'QmSK2tz19L38cQFZkAbSwtJ8cRXKjE8CPy73tPpFLz9DGc'
        receipt = test_datadownload(file_name, file_cid)
        print(receipt)
    elif(args.test_func==2):
        token_data = test_query(hash_ref)
        print(token_data)
    elif(args.test_func==3):
        recepit = test_register(hash_ref, json_ref)
        print(recepit)
    elif(args.test_func==4):
        recepit = test_burn(hash_ref, account_id)
        print(recepit)
    elif(args.test_func==5):
        if(args.op==1):
            to_address = getAddress('account1')
        else:     
            to_address = getAddress('account0')
        recepit = test_transfer(hash_ref, to_address)
        print(recepit)
    elif(args.test_func==6):
        data_tracker = test_tracker(hash_ref)
        print(data_tracker['hash'])
        for tracker in data_tracker['tracker']:
            print(tracker)   
    else:
        if(args.op==1):
            file_name = 'test_figure.png'
        else:     
            file_name = 'test_file.txt'
        receipt = test_dataupload(file_name)
        print(receipt)
