
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

## This class define initialization and provide wrapper of Box functions.
class Box(object):
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
	def store_token(self, token_num):
		tx_hash = self.contract.functions.store(int(token_num)).transact({'from': self.web3.eth.coinbase})
		return self.web3.eth.wait_for_transaction_receipt(tx_hash)

	## retrieve value
	def query_token(self):
		return self.contract.functions.retrieve().call({'from': self.web3.eth.coinbase})


if __name__ == "__main__":
	## configuratation
	httpProvider = Box.getAddress('HttpProvider')
	contractAddr = Box.getAddress('Box')
	contractConfig = '../build/contracts/Box.json'

	## new Box instance
	myBox = Box(httpProvider, contractAddr, contractConfig)

	## query local account and balance
	accounts = myBox.getAccounts()
	print("host accounts: %s" %(accounts))

	## store value to Box
	balance = myBox.getBalance(accounts[0])
	print("coinbase balance:%d" %(balance))

	## Retrive value from Box
	receipt = myBox.store_token(10)
	print(receipt)

	token_value = myBox.query_token()
	print(token_value)
