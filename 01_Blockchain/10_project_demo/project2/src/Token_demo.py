
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

	##  return balance of account  
	def getBalance(self, account_addr = ''):
		if(account_addr == ''):
			checksumAddr = self.web3.eth.coinbase
		else:
			checksumAddr = Web3.toChecksumAddress(account_addr)
		return self.web3.fromWei(self.web3.eth.getBalance(checksumAddr), 'ether')

	## get address from json file, helper function
	@staticmethod
	def getAddress(node_name):
		address_json = json.load(open('./addr_list.json'))
		return address_json[node_name]

	##------------------- Contract functions: store and retrive value -------------------------
	## store value
	def token_deposit(self, token_id, token_value, iswait=True):
		tx_hash = self.contract.functions.deposit(token_id, int(token_value)).transact({'from': self.web3.eth.coinbase})
		return self.web3.eth.wait_for_transaction_receipt(tx_hash)

	## store value
	def token_withdraw(self, token_id, token_value):
		tx_hash = self.contract.functions.withdraw(token_id, int(token_value)).transact({'from': self.web3.eth.coinbase})
		return self.web3.eth.wait_for_transaction_receipt(tx_hash)

	## retrieve value
	def token_query(self, token_id):
		return self.contract.functions.query(token_id).call({'from': self.web3.eth.coinbase})

	## set policy
	def token_setpolicy(self, token_id, token_policy):
		tx_hash = self.contract.functions.set_policy(token_id, token_policy).transact({'from': self.web3.eth.coinbase})
		return self.web3.eth.wait_for_transaction_receipt(tx_hash)

	## retrieve value
	def token_getpolicy(self, token_id):
		return self.contract.functions.get_policy(token_id).call({'from': self.web3.eth.coinbase})


if __name__ == "__main__":
	## configuratation
	httpProvider = Token.getAddress('HttpProvider')
	contractAddr = Token.getAddress('Token')
	contractConfig = '../build/contracts/Token.json'

	## new Token instance
	myToken = Token(httpProvider, contractAddr, contractConfig)

	## deposit Token
	print("token %d deposit value %d" %(1, 10))
	receipt = myToken.token_deposit(1, 10)
	# print(receipt)

	## query Token
	token_value = myToken.token_query(1)
	print("token %d has balance %d" %(1, token_value))


	## withdraw Token value less than balance
	print("token %d withdraw value %d" %(1, 5))
	receipt = myToken.token_withdraw(1, 5)
	# print(receipt)

	## query Token
	token_value = myToken.token_query(1)
	print("token %d has balance %d" %(1, token_value))


	## withdraw Token more than balance
	print("token %d withdraw value %d" %(1, token_value+1))
	receipt = myToken.token_withdraw(1, token_value+1)
	# print(receipt)

	## query Token
	token_value = myToken.token_query(1)
	print("token %d has balance %d" %(1, token_value))


	## set Token policy
	print("token %d set policy %s" %(1, "Test policy"))
	receipt = myToken.token_setpolicy(1, "Test policy")
	# print(receipt)

	## get Token policy
	token_policy = myToken.token_getpolicy(1)
	print("token %d has policy %s" %(1, token_policy))
