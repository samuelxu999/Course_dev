import ipfshttpclient

myclient = ipfshttpclient.connect('/dns/localhost/tcp/10206/http')  # Connects to: /dns/localhost/tcp/5001/http

## add a file under current directory
receipt = myclient.add('test_file.txt')
print(receipt)

hash_value = receipt['Hash']
# print(hash_value)

file_content = myclient.cat(hash_value)
print(file_content.decode("utf-8"))

## save content to a file
text_file = open("Output.txt", "w")

text_file.write(file_content.decode("utf-8"))

text_file.close()

## use get to download file
# file_content = myclient.get(hash_value)