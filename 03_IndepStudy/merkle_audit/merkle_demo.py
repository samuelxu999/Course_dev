import json
import requests
import argparse
import sys
import hashlib
from datetime import date, timedelta

## This class implement merkle tree operation
class MerkleTree:
    def __init__(self, data_blocks):
        self.data_blocks = data_blocks
        self.tree = self.build_tree(data_blocks)

    def build_tree(self, data_blocks):
         # Hash the data blocks
        hashed_data_blocks = [hashlib.sha256(block.encode('utf-8')).hexdigest() for block in data_blocks]
        if len(hashed_data_blocks) == 0:
            return None
        
        # Build the tree
        while len(hashed_data_blocks) > 1:
            if len(hashed_data_blocks) % 2 != 0:
                hashed_data_blocks.append(hashed_data_blocks[-1])
            new_level = []
            for i in range(0, len(hashed_data_blocks), 2):
                combined_hash = hashlib.sha256((hashed_data_blocks[i] + hashed_data_blocks[i+1]).encode('utf-8')).hexdigest()
                new_level.append(combined_hash)
            hashed_data_blocks = new_level
        return hashed_data_blocks[0]

    def get_root(self):
        return self.tree

## This function can load wearable data from a json file
def JSON_load(filepath):
  """
  Load JSON data from file
  """
  fname = open(filepath, 'r') 
  json_str=fname.read()
  fname.close()
  #json_data = json.loads(json_str)
  json_data=json.loads(json_str)
  return json_data

## This function create date range given startdate and enddate
def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days+1)
    for n in range(days):
        yield start_date + timedelta(n)

## This define arguments to test main funciton
def define_and_get_arguments(args=sys.argv[1:]):
  parser = argparse.ArgumentParser(
    description="Run test Fitbit API client."
  )
  parser.add_argument("--test_func", type=int, default=0, help="test function option.")

  args = parser.parse_args(args=args)
  return args

if __name__ == '__main__':
  ## get arguments
  args = define_and_get_arguments()

  test_func = args.test_func

  if(test_func == 1):
    ## ------------ set date range ----------------
    start_date = date(2025, 2, 14)
    end_date = date(2025, 2, 15)

    ## this ls_date store days that are used to load json file.
    ls_date = []
    for single_date in daterange(start_date, end_date):
        # print(single_date.strftime("%Y-%m-%d"))
        ls_date.append(single_date.strftime("%Y-%m-%d"))

    ## load data from json file from heartRate folder
    data_folder = "heartRate"
    ls_data = []
    for item in ls_date:
      filename = data_folder + "/" + item + ".json"
      load_data = JSON_load(filename)
      # print(load_data)
      ls_data.append(json.dumps(load_data))

    ## calculate merkle tree root
    merkle_tree = MerkleTree(ls_data)
    print(f"Merkle Root: {merkle_tree.get_root()}")

  else:    
    ## Example Usage
    data = ['data1', 'data2', 'data3', 'data4']
    merkle_tree = MerkleTree(data)
    print(f"Merkle Root: {merkle_tree.get_root()}")