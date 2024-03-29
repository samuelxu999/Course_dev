#!/usr/bin/env python3

'''
========================
PRC_ipfs module
========================
Created on Feb.20, 2024
@author: Xu Ronghua
@Email:  ronghuax@mtu.edu
@TaskDescription: This module provide encapsulation of RPC-JSON API that access to local IPFS node.
'''

import requests
import json
import time
import os
import pycurl
from io import BytesIO

class RPC_Curl(object):
	def __init__(self, rpc_port):
		self.rpc_port = str(rpc_port)

	'''
	To retrive a file content from IPFS, you just need the string’s hash. 
	curl -X POST "http://127.0.0.1:5001/api/v0/cat?arg=@hash"
	'''
	def retrive_file(self, ref_hash): 

		response = {}
		data_buffer = BytesIO() 
		crl = pycurl.Curl()

		# Set URL value
		crl.setopt(crl.URL, 'http://127.0.0.1:'+self.rpc_port+'/api/v0/cat?arg='+ref_hash)

		# Write bytes that are utf-8 encoded
		crl.setopt(crl.WRITEDATA, data_buffer)

		crl.setopt(crl.POST, 1)

		# Perform a file transfer 
		crl.perform() 

		# get status code
		response['status'] = crl.getinfo(pycurl.HTTP_CODE)

		# End curl session
		crl.close()

		# Get the content stored in the BytesIO object (in byte characters) 
		get_body = data_buffer.getvalue()

		# Decode the bytes stored in get_body and return the result
		response['results'] = get_body
		return response

	'''
	This can save a file on IPFS
	Execute: curl -F file=@test_file.txt -X POST "http://127.0.0.1:5001/api/v0/add"
	Return: hash of the address string of root directory of your file inside ipfs.
	'''
	def save_file(self, file_name): 
		response = {}
		body_buffer = BytesIO(''.encode('utf-8')) 
		crl = pycurl.Curl()

		# crl.setopt(crl.HTTPHEADER, ['Content-Type: text/plain'])

		# Set URL value
		crl.setopt(crl.URL, 'http://127.0.0.1:'+self.rpc_port+'/api/v0/add')

		crl.setopt(crl.POST, 1)

		crl.setopt(crl.HTTPPOST, [('data', (crl.FORM_FILE, file_name))])

		# Write response data into body_buffer
		crl.setopt(crl.WRITEDATA, body_buffer)

		# Perform a file transfer 
		crl.perform() 

		# get status code
		response['status'] = crl.getinfo(pycurl.HTTP_CODE)

		# End curl session
		crl.close()

		# Get the content stored in the BytesIO object (in byte characters) 
		get_body = body_buffer.getvalue()

		# Decode the bytes stored in get_body and return the result 
		response['results']  = get_body.decode('utf8')

		return response



def test():

	rpc_curl = RPC_Curl(10206)

	# file_name = 'test_file.txt'
	file_name = 'Gossip_protocol.jpg'

	post_ret = rpc_curl.save_file(file_name)
	# print(post_ret)
	print(json.loads(post_ret['results']))

	# # use string hash
	receipt = json.loads(post_ret['results'])
	ref_hash = receipt['Hash']
	download_file = "dl_"+receipt['Name']
	# print(download_file)

	## retrive file content from ipfs
	file_content = rpc_curl.retrive_file(ref_hash)['results']
	# print(file_content)

	## save content to a download_file with prefix 'dl'
	text_file = open(download_file, "wb")
	text_file.write(file_content)
	text_file.close()


if __name__ == "__main__":

	test()
	pass
