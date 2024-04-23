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
import hashlib

from middleware_token import Token
from RPC_ipfs import RPC_Curl

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

	token_value=myToken.token_query(json_req['hash_ref'])
	json_data['hash']= json_req['hash_ref']
	json_data['owner']= token_value[0]
	json_data['filename']= token_value[1]
	json_data['public']= token_value[2]
	json_data['size']= token_value[3]

	return jsonify(json_data), 201

## register data token given hash_ref
@app.route("/Token/register", methods=['POST'])
def token_register():
	##Token information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)
	hash_ref = json_req['hash_ref']
	json_ref = json_req['token_value']
	owner_id = json_ref ['file_owner']
	file_name = json_ref ['file_name']
	file_cid = json_ref ['file_cid']
	file_size = json_ref ['file_size']

	## register Token
	json_data={}
	try:
		print("token %s assign to owner: %s" %(hash_ref, owner_id))
		receipt = myToken.token_register(hash_ref, owner_id, file_name, file_cid, file_size)
		tx_hash = receipt.transactionHash
		json_data['tx_hash']=string_to_hex(tx_hash)
		json_data['results']="token {} assign to owner: {}".format(hash_ref, owner_id)
	except Exception as e:
		print("An exception occurred: %s", repr(e))
		json_data['results']="An exception occurred: {}".format(repr(e))
	finally:
		return jsonify(json_data), 201

## burn token given hash_ref
@app.route("/Token/burn", methods=['POST'])
def token_burn():
	##Token information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)
	hash_ref = json_req['hash_ref']
	account_id = json_req['account_id']

	json_data={}
	try:
		coin_account = ls_accounts[account_id]
		print("token %s burn by owner %s" %(hash_ref, coin_account))
		receipt = myToken.token_burn(hash_ref, account_id)
		tx_hash = receipt.transactionHash
		json_data['tx_hash']=string_to_hex(tx_hash)
		json_data['results']="token {} burn by owner {}".format(hash_ref, coin_account)
	except Exception as e:
		print("An exception occurred: %s", repr(e))
		json_data['results']="An exception occurred: {}".format(repr(e))
	finally:
		return jsonify(json_data), 201

	return jsonify(json_data), 201

## transfer a token to a user
@app.route("/Token/transfer", methods=['POST'])
def token_transfer():
	##Token information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)
	hash_ref = json_req['hash_ref']
	to_address = json_req['to_address']

	json_data={}
	try:
		print("token %s transfer to %s" %(hash_ref, to_address))
		receipt = myToken.token_transfer(hash_ref, to_address)
		tx_hash = receipt.transactionHash
		json_data['tx_hash']=string_to_hex(tx_hash)
		json_data['results']="token {} transfer to {}".format(hash_ref, to_address)
	except Exception as e:
		print("An exception occurred: %s", repr(e))
		json_data['results']="An exception occurred: {}".format(repr(e))
	finally:
		return jsonify(json_data), 201

	return jsonify(json_data), 201

## show tracker of data token
@app.route('/Token/tracker', methods=['GET'])
def tracker_quary():
	##Token information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)
	hash_ref = json_req['hash_ref']

	json_data={}

	ls_tracker = myToken.tracker_quary(hash_ref)
	json_data['hash']= json_req['hash_ref']
	json_data['tracker']= ls_tracker

	return jsonify(json_data), 201

## save data into ipfs
@app.route('/Data/upload', methods=['GET'])
def data_upload():
	##data information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)

	## upload data process
	file_name = json_req['file_name']
	post_ret = rpc_curl.save_file(file_name)
	json_results = json.loads(post_ret['results'])

	# print(json_results)


	## process receipt
	json_reference = {}
	json_reference['filename'] = json_results['Name']
	json_reference['public'] = json_results['Hash']
	json_reference['size'] = json_results['Size']


	## prepare response
	json_data={}

	# calculate hash vaule of data reference
	str_reference = json_to_string(json_reference).encode('utf-8')
	json_data['hash'] = hashlib.sha256(str_reference).hexdigest()
	json_data['filename'] = json_reference['filename']
	json_data['public'] = json_reference['public']
	json_data['size'] = json_reference['size']

	# json_data['receipt']=myToken.token_getpolicy(json_req['token_id'])

	return jsonify(json_data), 201

## download data into ipfs
@app.route('/Data/downlad', methods=['GET'])
def data_downlad():
	##data information missing
	if(request.data=='{}'):
		abort(401, {'message': 'Token information missing, deny access'})

	# parse data from request.data
	req_data=bytes_to_string(request.data)
	json_req = string_to_json(req_data)

	## download data process
	download_file = "dl_"+ json_req['filename']
	file_cid = json_req['public']
	# print(file_cid)

	## retrive file content from ipfs
	file_content = rpc_curl.retrive_file(file_cid)['results']
	# print(file_content)

	## save content to a download_file with prefix 'dl'
	text_file = open(download_file, "wb")
	text_file.write(file_content)
	text_file.close()

	## prepare response
	json_data={}
	json_data['results'] = "Download {} successfully.".format(download_file)
	return jsonify(json_data), 201

if __name__ == '__main__':
	## configuratation
	httpProvider = Token.getAddress('HttpProvider')
	contractAddr = Token.getAddress('Token')
	contractConfig = '../build/contracts/TokenData.json'

	rpc_curl = RPC_Curl(10206)

	## new Token instance
	myToken = Token(httpProvider, contractAddr, contractConfig)

	ls_accounts = myToken.getAccounts()

	app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)