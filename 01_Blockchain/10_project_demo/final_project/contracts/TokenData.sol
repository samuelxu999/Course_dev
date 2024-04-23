// contracts/Box.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract TokenData {
    /*
        Define struct to represent token data.
    */
    struct DataRef {
        address owner;      // address of data owner
        string name;   // file name of data content
        string cid;      //public cid of data on ipfs
        uint256 size;       // file size
    }

    /*
        Define struct to represent data tracker object.
    */
    struct DataTracker {
        address sender;     // from previous owner
        address receiver;   // to current owner
    }


    // Mapping from hash of Data reference to data reference
    mapping(bytes32 => DataRef) private data_reference;

    // Mapping from token ID to DataTracker (array)
    mapping(bytes32 => DataTracker[]) private dataTracker;

    // event handle function
    event On_RegisterChanged(bytes32 hash_ref);

    // event handle function
    event On_BurnChanged(bytes32 hash_ref);

    // event handle function
    event On_DataTracker_Update(bytes32 hash_ref, uint256 _value);

    // event handle function
    event On_PolicyChanged(string policy);

    // constructor() {
    //     _auth = new Auth(msg.sender);
    // }

    function register(bytes32 hash_ref, address owner_id, string memory file_name, string memory file_cid, uint256 file_size) public {
        require(data_reference[hash_ref].owner == address(0), "Register Data Token Fail: the data has owner.");
        
        // initialize a datatoken given hash_ref and input reference informaiton
        data_reference[hash_ref].owner = owner_id;
        data_reference[hash_ref].name = file_name;
        data_reference[hash_ref].cid = file_cid;
        data_reference[hash_ref].size = file_size;

        // initialize a DataTracker given hash_ref
        dataTracker[hash_ref].push( DataTracker(address(0), owner_id) );
        emit On_RegisterChanged(hash_ref);

    }

    function burn(bytes32 hash_ref) public {
        require(data_reference[hash_ref].owner == msg.sender, "Burn Data Token Fail: owner can burn data token.");
       
        // delete data token given hash_ref
        delete data_reference[hash_ref];
        
        // delete DataTracker given hash_ref
        delete dataTracker[hash_ref];
        emit On_BurnChanged(hash_ref);
    }

    function query(bytes32 hash_ref) public view returns (address, string memory, string memory, uint256) {
        return(data_reference[hash_ref].owner,
                data_reference[hash_ref].name,
                data_reference[hash_ref].cid,
                data_reference[hash_ref].size);
    }

    // get total tracker given a hash_ref
    function total_traker(bytes32 hash_ref) public view returns (uint256) {
        return dataTracker[hash_ref].length;
    }

    // query DataTracker given hash_ref and index
    function query_DataTracker(bytes32 hash_ref, uint256 index) public view returns (address, address) {
        require(index < dataTracker[hash_ref].length, "DataTracker: index out of bounds");

        return(dataTracker[hash_ref][index].sender, 
            dataTracker[hash_ref][index].receiver
            );      
    }

    //
    function transfer(bytes32 hash_ref, address to) public {
        uint256 index = dataTracker[hash_ref].length;
        index-=1;
        address from = dataTracker[hash_ref][index].receiver;
        require(from != to, "DataTracker: from and to address are the same");
        require(address(0) != to, "DataTracker: to address cannot be 0");
        // update tracker
        dataTracker[hash_ref].push( DataTracker(from, to) );

        emit On_DataTracker_Update(hash_ref, dataTracker[hash_ref].length);
    }

}