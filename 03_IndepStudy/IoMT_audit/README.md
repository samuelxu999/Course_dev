# This project uses NFT to provide identity authentication, data integrity, auditability, and tracability atop Ethereum.

The sample code demonstrates following case study:

1. Show how to implement a NFT smart contract that follows ERC-721

2. How to use Hardhat to perform unit test and scripting tasks on a Hardhat test network

3. How to use truffle to compile and deploy NFT contracts on a ganache test network

4. How to develop python wrapper class to interact with functions of NFT tokens. 

5. How to use python to showcase core functions and evaluate performance, such as latency and gas consumption. 

## Install required tools: ganache-cli and truffle
```shell
npm install -g ganache-cli
npm install -g truffle
``` 


## Use Hardhat to run test suites.

1) For hardhat installation:
```shell
npm install				// install packages and dependencies
npx hardhat help		// list help information for npx hardhat
```

2) You can launch a screen sesstion to launch a local hardhat for test. 
```shell
screen -S hardhat_node  // open a screen session called hardhat_node and attach it
npx hardhat node        // launch a local hardhat for test
ctrl+A+D 				// detach screen and leave node runing in background
screen -r hardhat_node  // attach hardhat_node screen session to get information
````

3) Run test cases on hardhat, you can try following commands. 
```shell
npx hardhat compile												// compile all contracts
npx hardhat test												// execute unit test cases
npx hardhat run --network localhost scripts/deploy.js			// deploy contracts on local hardhat network, use default port 8545
npx hardhat run --network localhost ./scripts/NFT_CapAC.demo.js	// execute NFT_CapAC.demo.js scripts
````

## You can also setup ganache as test network.

1) Opne a new terminal, then run ganache-cli:
```shell
screen -S ganache_node						// open a screen session called ganache_node and attach it
 ganache-cli -i 5777 --gasLimit 10000000 --port 8544		// launch a ganache-cli for ethereum test network, use port 8544.
ctrl+A+D 									// detach screen and leave node runing in background
screen -r ganache_node  					// attach ganache_node screen session to get information
``` 

2) compile contracts and migrate to local network.
```shell
// compile contracts
truffle compile	

// deploy contracts on local network
truffle migrate --reset
```

3) Preparation

a) After deploying a contract on test network, you need write down "contract address" and replace it in addr_list.json given contract name.

b) Install required dependecies
```shell
python3 -m pip install -r requirements.txt
```

4) To run test cases in /src, you can execute the following commands.
```shell
cd src
// execute demo test cases (py), e.g,. NFT_CapAC.py
python3 NFT_CapAC.py -h  						// get usages
python3 NFT_CapAC.py --test_op 0				// display all accounts
python3 NFT_CapAC.py --test_op 1 --id token1	// query token1 
python3 NFT_CapAC.py --test_op 2 --id token1 --op_status 0	// mint token1 by owner
python3 NFT_CapAC.py --test_op 2 --id token2 --op_status 1	// mint token2 by other
python3 NFT_CapAC.py --test_op 3 --id token1	// burn token1
python3 NFT_CapAC.py --test_op 4 --id token1	// update AC expired date of token1
python3 NFT_CapAC.py --test_op 5 --id token1 --value "Assign access right!" // assign access rights to token1
python3 NFT_CapAC.py --test_op 6 --id token1 --value "0x5aa101f0ec62a04329d2db2e8763c55cc10ba3d7a6a08f4557aa15159ce3a7c9" // add patient id to token1
python3 NFT_CapAC.py --test_op 7 --id token1 --value "QmSK2tz19L38cQFZkAbSwtJ8cRXKjE8CPy73tPpFLz9DGc" // add data reference to token1
````

5) To run latency test case in /src, you can execute the following commands.
```shell
cd src
// execute demo test cases (py), e.g,. test_demo.py
python3 test_demo.py -h  							// get usages

python3 test_demo.py --test_func 0					// display all accounts and tokens

python3 test_demo.py --test_func 1 --tx_round 5		// query token data (id start from 1) 

python3 test_demo.py --test_func 2 --value host_account --tx_round 5	// mint token by its owner

python3 test_demo.py --test_func 4 --tx_round 5 	// add patient id (random hash string) into token data

python3 test_demo.py --test_func 5 --value 100 --tx_round 5 	// add data reference (a list of random data) into token data

python3 test_demo.py --test_func 6 --tx_round 5 	// Add access rights (json format) into token data

python3 test_demo.py --test_func 3 --tx_round 5		// burn token (id start from 1)
````