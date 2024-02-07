# Sample Smart Contract Project for learning process

This project demonstrates a simple smart contract case:
1) Show how to use Hardhat test network to test smart contract without running ehtereum

2) Show how to use truffle to compile and deploy chain code on a local ethereum network, then develop python wrapper to interact with smart contract.


## Organization of project
|   name   | Description |
|:----------:|-------------|
| contracts | contain all smart contract source files (*.sol). |ß
| scripts | scrpts directory containing deploy.js and other demo cases, e.g,. index.js. |
| test | unit test folder containeing all test cases file (*.js). |
| src | contrain config, requirements, and python demo code. |
| hardhat.config.js | configuration file for hardhat environment. |
| package.json | save all dependencies and packages for node.js. |
| truffle-config.js | configuration file for truffle environment. |


## Preparation
1) install truffle:
```shell
npm install -g truffle
```

2) install Hardhat and other packages
```shell
npm install				// install items from package.json
npx hardhat help		// list help information for npx hardhat	
```

3) For hardhat.config.js and truffle-config.js, you need to change compilers-->solc to current solidity verions. 

To check current solidity version:
```shell
truffle version
```

## Using Hardhat to compile, deploy and test smart contracts
### 1) compile and run unit test:
```shell
npx hardhat compile		// compile all contracts
npx hardhat test		// execute unit test cases
```

### 2) deploy smart contrac on local hardhat test network and run demo
a) First of all, you need launch a local hardhat test network and let it run background.

```shell
screen -S hardhat_node  // open a screen session called hardhat_node and attach it
npx hardhat node        // launch a local hardhat for test
ctrl+A+D 				// detach screen and leave node runing in background
screen -r hardhat_node  // attach hardhat_node screen session
```

b) deploy contracts on local hardhat network
```shell
npx hardhat run --network localhost scripts/deploy.js
```

b) Open index.js then update 'const address' to just deployed smart contract address.

c) execute scripts to run demo cases of smart contract on local hardhat network.
```shell
npx hardhat run --network localhost ./scripts/index.js	// execute scripts
```

## You can also setup local miners as test network.

You need check these points:

-- ensure local miners are running

-- enable networks->development in truffle-config.js 

-- correct deploy functions in 2_deploy_contracts.js

1) compile contracts and migrate to local network.
```shell
// compile contracts
truffle compile	

// deploy contracts on local network (enable networks->development in truffle-config.js)
truffle migrate --reset
````

2) To test on local network, you can try following commands.
```shell
cd src
// execute demo test cases (py)
python3 Box_demo.py
````