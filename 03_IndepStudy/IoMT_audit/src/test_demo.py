'''
========================
test_demo
========================
Created on July.22, 2024
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module provide test cases for demo and performance analysis.
'''

import datetime, time
import logging
import argparse
import sys
import os
import threading

from merkletree import MerkleTree
from utilities import DatetimeUtil, TypesUtil, FileUtil, FuncUtil
from NFT_CapAC import NFT_CapAC

logger = logging.getLogger(__name__)

## ------------------- global variable ----------------------------
httpProvider = NFT_CapAC.getAddress('HttpProvider')

## new NFT_CapAC instance
contractAddr = NFT_CapAC.getAddress('NFT_CapAC')
contractConfig = '../build/contracts/NFT_CapAC.json'
token_dataAC = NFT_CapAC(httpProvider, contractAddr, contractConfig)

accounts = token_dataAC.getAccounts()
base_account = accounts[0]



## ---------------------- Internal function and class -----------------------------
def query_token(tokenId):
	token_value = token_dataAC.query_CapAC(tokenId)
	owner = token_dataAC.ownerToken(tokenId)
	print("Token_id:{}   owner:{}  CapAC:{}".format(tokenId, owner, token_value))
	return token_value


def mint_token(tokenId, owner):
	_account = NFT_CapAC.getAddress(owner)

	receipt = token_dataAC.mint_CapAC(tokenId, _account)
	_owner = token_dataAC.ownerToken(tokenId)

	if(receipt!=None):
		print('Token {} is mint by {}'.format(tokenId, _owner))
	else:
		print('Token {} has been mint by {}'.format(tokenId, _owner))

	return receipt

def burn_token(tokenId):
	_owner = token_dataAC.ownerToken(tokenId)
	receipt = token_dataAC.burn_CapAC(tokenId)

	if(receipt!=None):
		print('Token {} is burn by owner {}'.format(tokenId, _owner))
	else:
		print('Token {} is not existed'.format(tokenId))

	return receipt

def test_DataRef(tokenId, ls_args):
	_owner = token_dataAC.ownerToken(tokenId)
	if(_owner==None):
		print('Token {} is not existed'.format(tokenId))
		return

	print('Token {} setCapAC_datareference.'.format(tokenId))
	receipt = token_dataAC.CapAC_datareference(tokenId, ls_args[0])

	return receipt

def test_PatientID(tokenId):
	_owner = token_dataAC.ownerToken(tokenId)
	if(_owner==None):
		print('Token {} is not existed'.format(tokenId))
		return

	print('Token {} setCapAC_patientid.'.format(tokenId))
	patient_id = TypesUtil.string_to_hex(os.urandom(32))
	receipt = token_dataAC.CapAC_patientid(tokenId, patient_id)

	return receipt

def test_CapAC(tokenId):
	_owner = token_dataAC.ownerToken(tokenId)
	if(_owner==None):
		print('Token {} is not existed'.format(tokenId))
		return

	print('Token {} setCapAC_authorization.'.format(tokenId))
	# patient_id = TypesUtil.string_to_hex(os.urandom(32))

	access_right = {}
	access_right['resource']="/test/api/v1.0/dt"
	access_right['action']="GET"
	access_right['conditions']={"value": {"start": "9:00:00", "end": "15:30:00"},"type": "Timespan"}
	str_ac = TypesUtil.json_to_string(access_right)

	receipt = token_dataAC.CapAC_authorization(tokenId, str_ac)

	return receipt

def dummy_data(value=1):

	# ## get mkt_root
	# mkt_root = TypesUtil.string_to_hex(os.urandom(64)) 

	## get hash value of data
	ls_data = []
	for i in range(value):
		ls_data.append( TypesUtil.string_to_hex(os.urandom(128)) )

	## build a Merkle tree from ls_data list
	merkle_tree = MerkleTree(ls_data)

	## get merkle root
	mkt_root = merkle_tree.get_root()

	parameters = [mkt_root, ls_data]

	return parameters

def define_and_get_arguments(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(
	    description="Run test demo."
	)

	parser.add_argument("--tx_round", type=int, default=1, 
						help="tx evaluation round")

	parser.add_argument("--wait_interval", type=int, default=1, 
	                    help="break time between tx evaluate step.")

	parser.add_argument("--test_func", type=int, default=0, 
	                    help="Execute test function: \
	                    0-contract information, \
	                    1-query_token, \
	                    2-mint_token, \
	                    3-burn_token, \
	                    4-test_DataRef, \
	                    5-test_Patient, \
	                    6-test_CapAC")

	parser.add_argument("--op_status", type=int, default=0, 
	                    help="operation status: based on app")

	parser.add_argument("--id", type=int, default=1, 
	                    help="input token id (int)")
	parser.add_argument("--value", type=str, default="", 
	                    help="input token value (string)")

	parser.add_argument("--data_size", type=int, default=128, 
						help="Size (KB) of randome data for test.")

	args = parser.parse_args(args=args)
	return args

if __name__ == "__main__":
	# Logging setup
	FORMAT = "%(asctime)s | %(message)s"
	logging.basicConfig(format=FORMAT)
	logger.setLevel(level=logging.DEBUG)

	args = define_and_get_arguments()

	## switch test cases
	if(args.test_func==1):
		for i in range(args.tx_round):			
			logger.info("Test run:{}".format(i+1))
			ls_time_exec = []
			token_id = args.id + i
			start_time=time.time()
			query_token(token_id) 
			logger.info("exec_time: {} ms".format( format( (time.time()-start_time)*1000, '.3f')  ))
			ls_time_exec.append(format( (time.time()-start_time)*1000, '.3f' ))
			str_time_exec=" ".join(ls_time_exec)
			FileUtil.save_testlog('test_results', 'query_tokenData.log', str_time_exec)
			time.sleep(args.wait_interval)
	elif(args.test_func==2):
		for i in range(args.tx_round):
			logger.info("Test run:{}".format(i+1))
			token_id = args.id + i
			ls_time_exec = []
			start_time=time.time()
			receipt = mint_token(token_id, args.value)
			if(receipt!=None):
				logger.info("exec_time: {} sec   gasUsed: {}".format( format( time.time()-start_time, '.3f'), receipt['gasUsed'] ))
				ls_time_exec.append( format( time.time()-start_time, '.3f') )
				str_time_exec=" ".join(ls_time_exec)
				FileUtil.save_testlog('test_results', 'mint_tokenData.log', str_time_exec)
			time.sleep(args.wait_interval)
	elif(args.test_func==3):
		for i in range(args.tx_round):
			logger.info("Test run:{}".format(i+1))
			token_id = args.id + i
			ls_time_exec = []
			start_time=time.time()
			receipt = burn_token(token_id)
			if(receipt!=None):
				logger.info("exec_time: {} sec   gasUsed: {}".format( format( time.time()-start_time, '.3f'), receipt['gasUsed'] ))
				ls_time_exec.append( format( time.time()-start_time, '.3f') )
				str_time_exec=" ".join(ls_time_exec)
				FileUtil.save_testlog('test_results', 'burn_tokenData.log', str_time_exec)

			time.sleep(args.wait_interval)
	elif(args.test_func==4):
		for i in range(args.tx_round):
			logger.info("Test run:{}".format(i+1))
			token_id = args.id + i
			
			ls_time_exec = []
						
			start_time=time.time()
			receipt = test_PatientID(token_id)
			if(receipt!=None):
				logger.info("exec_time: {} sec   gasUsed: {}".format( format( time.time()-start_time, '.3f'), receipt['gasUsed'] ))
				ls_time_exec.append( format( time.time()-start_time, '.3f') )
				str_time_exec=" ".join(ls_time_exec)
				FileUtil.save_testlog('test_results', 'update_Patient.log', str_time_exec)
			time.sleep(args.wait_interval)
	elif(args.test_func==5):
		for i in range(args.tx_round):
			logger.info("Test run:{}".format(i+1))
			token_id = args.id + i
			
			ls_time_exec = []
			start_time=time.time()

			## get dummy data for test
			ls_parameters = dummy_data(int(args.value))	

			# print(ls_parameters)
			ls_time_exec.append( format( time.time()-start_time, '.3f') )
			
			start_time=time.time()
			receipt = test_DataRef(token_id, ls_parameters)
			if(receipt!=None):
				logger.info("exec_time: {} sec   gasUsed: {}".format( format( time.time()-start_time, '.3f'), receipt['gasUsed'] ))
				ls_time_exec.append( format( time.time()-start_time, '.3f') )
				str_time_exec=" ".join(ls_time_exec)
				FileUtil.save_testlog('test_results', 'update_DataRef.log', str_time_exec)
			time.sleep(args.wait_interval)
	elif(args.test_func==6):
		for i in range(args.tx_round):
			logger.info("Test run:{}".format(i+1))
			token_id = args.id + i
			
			ls_time_exec = []
						
			start_time=time.time()
			receipt = test_CapAC(token_id)
			if(receipt!=None):
				logger.info("exec_time: {} sec   gasUsed: {}".format( format( time.time()-start_time, '.3f'), receipt['gasUsed'] ))
				ls_time_exec.append( format( time.time()-start_time, '.3f') )
				str_time_exec=" ".join(ls_time_exec)
				FileUtil.save_testlog('test_results', 'update_CapAC.log', str_time_exec)
			time.sleep(args.wait_interval)

	else:
		balance = token_dataAC.getBalance(base_account)
		print("coinbase account: {}   balance: {}".format(base_account, balance))

		ls_token = []
		total_supply = token_dataAC.query_totalSupply()
		print("DataAC total supply: %d" %(total_supply))
		for idx in range(total_supply):
			ls_token.append(token_dataAC.query_tokenByIndex(idx))
		print(ls_token)
