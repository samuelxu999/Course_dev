# IPFS Project

This project demonstrates a simple IPFS-based distributed storage:
1) Show how to use sh and yml to manage ipfs nodes

2) Show how to use python to implement ipfs http client wrapper.


## Organization of project
|   name   | Description |
|:----------:|-------------|
| demo_case | sh scripts to run single ipfs node. |
| ipfs_client | py scripts that encapsulate http functions for ipfs data put and get. |
| docker-compose.yml | using docker-compose to manage a swarm of ipfs nodes |
| setup.txt | Envrionment setup and ipfs operations. |


## Run docker-compose.yml 
1) start ipfs containers:
```shell
docker-compose up -d
```

2) stop ipfs containers
```shell
docker-compose down 	
```

3) check running ipfs containers. 
```shell
docker-compose ps
```