import ipfshttpclient

myclient = ipfshttpclient.connect('/dns/localhost/tcp/10206/http')  # Connects to: /dns/localhost/tcp/5001/http

## add a file under current directory
# file_name = 'test_file.txt' 
file_name = 'Gossip_protocol.jpg'
receipt = myclient.add(file_name)

print(receipt)

## retrive file from ipfs
hash_value = receipt['Hash']
download_file = "dl_"+receipt['Name']
# print(download_file)

## retrive file content from ipfs
file_content = myclient.cat(hash_value)
# print(file_content.decode("utf-8"))

## save content to a download_file with prefix 'dl'
text_file = open(download_file, "wb")
text_file.write(file_content)
text_file.close()

## use get to download file
# file_content = myclient.get(hash_value)