'''
========================
Server_Token module
========================
Created on March.14, 2024
@author: Xu Ronghua
@Email:  ronghuax@mtu.edu
@TaskDescription: This module provide encapsulation of toekn demo API that handle and response client's request.
'''

import time
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, jsonify
from flask import abort,make_response,request

from Token_demo import Token

app = Flask(__name__)

def bytes_to_string(byte_data):
	str_data=byte_data.decode(encoding='UTF-8')
	return str_data

def string_to_bytes(str_data):
	bytes_data=str_data.encode(encoding='UTF-8')
	return bytes_data

def string_to_json(json_str):
	json_data = json.loads(json_str)
	return json_data

def json_to_string(json_data):
	json_str = json.dumps(json_data)
	return json_str

def hex_to_string(hex_data):
	str_data=bytes.fromhex(hex_data)
	return str_data

def string_to_hex(str_data):
	hex_data=str_data.hex()
	return hex_data

def int_to_hex(int_data):
	return hex(int_data)
	

def hex_to_int(hex_data):
	return int(hex_data, 16)

#========================================== Error handler ===============================================
#Error handler for abort(404) 
@app.errorhandler(404)
def not_found(error):
    #return make_response(jsonify({'error': 'Not found'}), 404)
    response = jsonify({'result': 'Failed', 'message':  error.description['message']})
    response.status_code = 404
    return response

#Error handler for abort(400) 
@app.errorhandler(400)
def type_error(error):
    #return make_response(jsonify({'error': 'type error'}), 400)
    response = jsonify({'result': 'Failed', 'message':  error.description['message']})
    response.status_code = 400
    return response
    
#Error handler for abort(401) 
@app.errorhandler(401)
def access_deny(error):
    response = jsonify({'result': 'Failed', 'message':  error.description['message']})
    response.status_code = 401
    return response

#========================================== Request handler ===============================================	
## query balance for specific token_id
@app.route('/Token/query', methods=['GET'])
def token_query():
	##Token information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)
	# print(json_req['token_id'])

	json_data={}

	json_data['id']= json_req['token_id']
	json_data['balance']=myToken.token_query(json_req['token_id'])

	return jsonify(json_data), 201

## deposit balance for specific token_id
@app.route("/Token/deposit", methods=['POST'])
def token_deposit():
	##Token information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)

	receipt = myToken.token_deposit(json_req['token_id'], json_req['token_value'])
	tx_hash = receipt.transactionHash

	json_data={}
	json_data['hash']=string_to_hex(tx_hash)

	return jsonify(json_data), 201

## withdraw balance for specific token_id
@app.route("/Token/withdraw", methods=['POST'])
def token_withdraw():
	##Token information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)

	receipt = myToken.token_withdraw(json_req['token_id'], json_req['token_value'])
	tx_hash = receipt.transactionHash

	json_data={}
	json_data['hash']=string_to_hex(tx_hash)

	return jsonify(json_data), 201

## set policy for specific token_id
@app.route("/Token/setpolicy", methods=['POST'])
def token_setpolicy():
	##Token information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)

	receipt = myToken.token_setpolicy(json_req['token_id'], json_req['token_policy'])
	tx_hash = receipt.transactionHash

	json_data={}
	json_data['hash']=string_to_hex(tx_hash)

	return jsonify(json_data), 201

## get policy  for specific token_id
@app.route('/Token/getpolicy', methods=['GET'])
def token_getpolicy():
	##Token information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)

	json_data={}

	json_data['id']= json_req['token_id']
	json_data['policy']=myToken.token_getpolicy(json_req['token_id'])

	return jsonify(json_data), 201


if __name__ == '__main__':
	## configuratation
	httpProvider = Token.getAddress('HttpProvider')
	contractAddr = Token.getAddress('Token')
	contractConfig = '../build/contracts/Token.json'

	## new Token instance
	myToken = Token(httpProvider, contractAddr, contractConfig)

	app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)