#!/bin/bash

NODE_NAME="node1"

IPFS_TEST="/home/rxu22/Github/Course_dev/01_Blockchain/02_IPFS/ipfs_test"
IPFS_SWARM_KEY_FILE="$IPFS_TEST/swarm.key"
IPFS_STAGING="$IPFS_TEST/$NODE_NAME/staging"
IPFS_DATA="$IPFS_TEST/$NODE_NAME/data"

container_name="ipfs_node1"
p2p_port=4001
rpc_port=5001
gateway_port=8081

docker run -d --rm \
--name $container_name \
-e $IPFS_SWARM_KEY_FILE= \
-v $IPFS_STAGING:/export \
-v $IPFS_DATA:/data/ipfs \
-p $p2p_port:4001 \
-p $p2p_port:4001/udp \
-p 127.0.0.1:$gateway_port:8080 \
-p 127.0.0.1:$rpc_port:5001 \
ipfs/kubo:latest
