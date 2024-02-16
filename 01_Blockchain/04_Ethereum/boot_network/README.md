## boot_network
Set up a private ethereum network on single host machine, including:


### bootnode
bootstrap node configuration and startup scripts on Ubuntu OS or mac. 

--- startbootnode.sh: start up bootnode, port-30301.

--- node_data:

    --- genesis.json: genesis data for private blockchain network initialization.

    --- password.sec: default password for a geth coinbase account.

### node1
node1 configuration and startup scripts on Ubuntu OS or mac. 

--- startnode1.sh: start up ethereum client as miner1, ipc-8042, port-30303.

--- node_data:

    --- genesis.json: genesis data for private blockchain network initialization.

    --- password.sec: default password for a geth coinbase account.


### node2
node2 configuration and startup scripts on OS or mac. 

--- startminer2.sh: start up ethereum client as miner2, pc-8043, port-30304.

--- node_data:

	--- genesis.json: genesis data for private blockchain network initialization.

	--- password.sec: default password for a geth coinbase account.

### Launch bootnode
Startup bootstrap node: open a new terminal, then execute `cd bootnode; ./startbootnode.sh`

With the bootnode online, it will display an enode URL that other nodes can use to connect to it and exchange peer information. 

### To setup bootnodes information for node1 and node2, you need open node1/startnode1.sh and node1/startnode1.sh, then use displayed enode URL on bootnode console to update --bootnodes @enode_URL.


### Launch peers: node1 and node2
Startup node1: open a new terminal, then execute `cd node1; ./startnode1.sh`

Startup node2: open a new terminal, then execute `cd node2; ./startnode2.sh`

With the peers online, they will discover each other through bootnode. 

### Attach to console
Attach node1 console: `geth attach node1/account/geth.ipc`

Attach node2 console: `geth attach node2/account/geth.ipc`

### get enode or peer information
After attach console, run following commands to get information:

> eth.accounts									(list all accounts)

> admin.nodeInfo.enode							(show enode data)

> admin.peers									(Show peers information)

> miner.start(1)								(Using 1 code to mine blocks)

> miner.stop()									(Stop mining blocks)

> web3.fromWei(eth.getBalance(eth.coinbase))	(Display mined ether coins)

> eth.blockNumber								(Show total blocks)

Transfer coins between accounts:
> eth.sendTransaction({from:eth.coinbase, to:"0xa79fd8f95fe0cfaf4536ed6292b9388355d39842", value:web3.toWei(100,"ether")})

Query transaction and block:
> eth.getTransaction(“@tx_receipt”)				(Get transaction data given a tx hash)

> eth.getBlock(@blockNumber)					(Get a block data given a block number as index)

