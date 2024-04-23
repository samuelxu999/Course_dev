// contracts/Box.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract Token {
    /*
        Define struct to represent token data.
    */
    struct TokenData {
        uint256 balance;        // balance value
        string policy;   // authronized access rights
    }

    // Mapping from token ID to token
    mapping(uint256 => TokenData) private tokendata;

    // event handle function
    event On_ValueChanged(uint256 value);

    // event handle function
    event On_PolicyChanged(string policy);

    // constructor() {
    //     _auth = new Auth(msg.sender);
    // }

    function deposit(uint256 token_id, uint256 value) public {
        tokendata[token_id].balance += value;
        emit On_ValueChanged(value);
    }

    function withdraw(uint256 token_id, uint256 value) public {
        if(tokendata[token_id].balance>=value) {
            tokendata[token_id].balance -= value;
        }
        emit On_ValueChanged(value);
    }

    function query(uint256 token_id) public view returns (uint256) {
        return tokendata[token_id].balance;
    }

    function set_policy(uint256 token_id, string memory policy) public {
        tokendata[token_id].policy = policy;
        emit On_PolicyChanged(policy);
    }

    function get_policy(uint256 token_id) public view returns (string memory) {
        return tokendata[token_id].policy;
    }
}