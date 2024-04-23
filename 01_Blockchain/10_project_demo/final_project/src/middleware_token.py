
'''
========================
Box_demo module
========================
@TaskDescription: This module provide encapsulation of web3.py API to interact with Box smart contract.
'''
from web3 import Web3, HTTPProvider, IPCProvider
import json, datetime, time
import sys
import argparse

## This class define initialization and provide wrapper of Token functions.
class Token(object):
	def __init__(self, http_provider, contract_addr, contract_config):
		## configuration initialization
		self.web3 = Web3(HTTPProvider(http_provider))
		self.contract_address = Web3.toChecksumAddress(contract_addr)
		self.contract_config = json.load(open(contract_config))

		## new contract object
		self.contract = self.web3.eth.contract(address=self.contract_address, 
		                                    abi=self.contract_config['abi'])

	##------------------- test functions: interact with local geth-client-------------------------
	## return accounts address
	def getAccounts(self):
		return self.web3.eth.accounts

	## get address from json file, helper function
	@staticmethod
	def getAddress(node_name):
		address_json = json.load(open('./addr_list.json'))
		return address_json[node_name]

	##------------------- Contract functions -------------------------
	## token registration-mint a data token
	def token_register(self, hash_ref, owner_id, file_name, file_cid, file_size, account_id=0):
		account_address = self.web3.eth.accounts[account_id]
		tx_hash = self.contract.functions.register(hash_ref, owner_id, file_name, file_cid, int(file_size)).transact({'from': account_address})
		return self.web3.eth.wait_for_transaction_receipt(tx_hash)

	## burn a data token
	def token_burn(self, hash_ref, account_id=0):
		account_address = self.web3.eth.accounts[account_id]
		tx_hash = self.contract.functions.burn(hash_ref).transact({'from': account_address})
		return self.web3.eth.wait_for_transaction_receipt(tx_hash)

	## retrieve data token
	def token_query(self, hash_ref):
		return self.contract.functions.query(hash_ref).call({'from': self.web3.eth.coinbase})

	## list all tracker for token data transfer
	def tracker_quary(self, hash_ref, account_id=0):
		account_address = self.web3.eth.accounts[account_id]
		total_tracker = self.contract.functions.total_traker(hash_ref).call({'from': account_address})
		ls_tracker=[]
		for idx in range(total_tracker):
			ls_tracker.append(self.contract.functions.query_DataTracker(hash_ref, idx).call({'from': account_address}))

		return ls_tracker

	## transfer a data token
	def token_transfer(self, hash_ref, to_address, account_id=0):
		account_address = self.web3.eth.accounts[account_id]
		tx_hash = self.contract.functions.transfer(hash_ref, to_address).transact({'from': account_address})
		return self.web3.eth.wait_for_transaction_receipt(tx_hash)



if __name__ == "__main__":
	## configuratation
	httpProvider = Token.getAddress('HttpProvider')
	contractAddr = Token.getAddress('Token')
	contractConfig = '../build/contracts/TokenData.json'


	## new Token instance
	myToken = Token(httpProvider, contractAddr, contractConfig)

	ls_accounts = myToken.getAccounts()

	hash_ref = '0x5aa101f0ec62a04329d2db2e8763c55cc10ba3d7a6a08f4557aa15159ce3a7c9'	
	owner_id = Token.getAddress('account0')
	file_name = "test_file.txt"
	file_cid = "QmSK2tz19L38cQFZkAbSwtJ8cRXKjE8CPy73tPpFLz9DGc"
	file_size = 22

	## register Token
	try:
		print("token %s assign to owner: %s" %(hash_ref, owner_id))
		receipt = myToken.token_register(hash_ref, owner_id, file_name, file_cid, file_size)
		# print(receipt)
	except Exception as e:
		print("An exception occurred: %s", repr(e))

	## query Token
	token_value = myToken.token_query(hash_ref)
	# print("token %d has data reference %s" %(hash_ref, token_value))
	print(token_value)


	## check all data tranfer tracker
	ls_tracker = myToken.tracker_quary(hash_ref)
	print(ls_tracker)

	## transfer a token
	try:
		
		to_address = Token.getAddress('account2')
		print("token %s transfer to %s" %(hash_ref, to_address))
		receipt = myToken.token_transfer(hash_ref, to_address)
		# print(receipt)
	except Exception as e:
		print("An exception occurred: %s", repr(e))

	## check all data tranfer tracker
	ls_tracker = myToken.tracker_quary(hash_ref)
	print(ls_tracker)


	## burn Token by owner
	try:
		account_id = 0
		coin_account = ls_accounts[account_id]
		print("token %s burn by owner %s" %(hash_ref, coin_account))
		receipt = myToken.token_burn(hash_ref, account_id)
		# print(receipt)
	except Exception as e:
		print("An exception occurred: %s", repr(e))

	## query Token again
	token_value = myToken.token_query(hash_ref)
	# print("token %d has data reference %s" %(hash_ref, token_value))
	print(token_value)

	# ## set Token policy
	# print("token %d set policy %s" %(1, "Test policy"))
	# receipt = myToken.token_setpolicy(1, "Test policy")
	# # print(receipt)

	# ## get Token policy
	# token_policy = myToken.token_getpolicy(1)
	# print("token %d has policy %s" %(1, token_policy))
