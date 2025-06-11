'''
========================
app_server module
========================
Created on June.11, 2025
@author: Xu Ronghua
@Email:  ronghuax@mtu.edu
@TaskDescription: This module provide webservice APIs for GUI pages
'''

import sys
import time
import datetime
import json
import threading
import logging
import asyncio
import socket

from flask import Flask, jsonify, render_template
from flask import abort,make_response,request
from argparse import ArgumentParser

## import contract wrapper
from Box_demo import Box

logger = logging.getLogger(__name__)

# ================================= Instantiate the server =====================================
app = Flask(__name__)



## ============================== Internal functions ==================================
def string_to_hex(str_data):
    hex_data=str_data.hex()
    return hex_data


#===================================== Web App handler ===================================
@app.route('/')
def info():
    ls_accounts = []
    ## query information of accounts by host
    accounts = myBox.getAccounts()

    for account in accounts:
        account_info={}
        account_info['account']=account
        account_info['balance'] = myBox.getBalance(account)

        ls_accounts.append(account_info)

    return render_template('info.html', posts = [ls_accounts, len(ls_accounts)])

@app.route('/queryToken', methods=['GET', 'POST'])
def queryToken():
    ret_posts = ['NULL']
    ## get params from request
    if request.method == 'POST':
        token_id = request.form.get('token_id')
        ret_posts[0]=token_id
        
        if(ret_posts[0]==''):
            ret_posts[0]='NULL'
        else:
            try:
                ## get token information
                token_value = myBox.query_token()

                ret_posts.append(token_value)

            except Exception as e:
                ret_posts[0] = 'Fail'
                ret_posts.append(str(e))

    return render_template('queryToken.html', posts = ret_posts)

@app.route('/storeToken', methods=['GET', 'POST'])
def storeToken():
    ret_posts = ['NULL']
    ## get params from request
    if request.method == 'POST':
        token_id = request.form.get('token_id')
        token_value = request.form.get('token_value')

        ret_posts[0]=token_id
        
        ## validate input: token id and token value
        if( (ret_posts[0]=='') or (not token_value.isdigit()) ):
            ret_posts[0]='NULL'
        else:
            try:

                ## store token value
                receipt = myBox.store_token(token_value)

                ## save transaction receipt to show results 
                ret_posts.append(token_value)

                ## save receipt information into results
                json_results = {}

                json_results['transactionHash'] = string_to_hex(receipt['transactionHash'])
                json_results['blockNumber'] = receipt['blockNumber']
                json_results['blockHash'] = string_to_hex(receipt['blockHash'])
                ret_posts.append(json_results)

            except Exception as e:
                ret_posts[0] = 'Fail'
                ret_posts.append(str(e))

    return render_template('storeToken.html', posts = ret_posts)

def define_and_get_arguments(args=sys.argv[1:]):
    parser = ArgumentParser(description="Run Box GUI server.")

    parser.add_argument("--debug", action="store_true", 
                        help="if set, debug model will be used.")

    parser.add_argument("--threaded", action="store_true", 
                        help="if set, support threading request.")

    parser.add_argument('-p', '--port', default=8080, type=int, 
                        help="http service port to listen on.")


    args = parser.parse_args()

    return args

## ****************************** Main function ***********************************
if __name__ == '__main__':
    FORMAT = "%(asctime)s %(levelname)s %(filename)s(l:%(lineno)d) - %(message)s"
    # FORMAT = "%(asctime)s %(levelname)s | %(message)s"
    LOG_LEVEL = logging.INFO
    logging.basicConfig(format=FORMAT, level=LOG_LEVEL)

    ## get arguments
    args = define_and_get_arguments()

    ## Box contract configuratation
    httpProvider = Box.getAddress('HttpProvider')
    contractAddr = Box.getAddress('Box')
    contractConfig = '../build/contracts/Box.json'

    ## new Box instance
    myBox = Box(httpProvider, contractAddr, contractConfig)


    ## -------------------------------- run app server ----------------------------------------
    app.run(host='0.0.0.0', port=args.port, debug=args.debug, threaded=args.threaded)


