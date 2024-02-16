#!/bin/sh

## Set key folder path
KEY_DIR="./account/keystore"
Account_dir="./account"
Node_dir="./node_data"

## check if main account is available
if ! [ "$(/bin/ls -A $KEY_DIR)" ]; then
	## new account dir
	mkdir $Account_dir

	## Initialize miners
	geth --datadir $Account_dir init $Node_dir/genesis.json

fi

## create boot.key
bootnode --genkey boot.key

## launch a bootstrap node
bootnode --nodekey boot.key --addr ":30301" 
