# Flask demo for Webservice 

Motivation: instruct how to use flask to build webservice APIs for network applications. 

### Set up python-flask 
1. Installing pip
```bash
sudo apt-get install python-pip
```
2. Installing Flask 
```bash
sudo pip install flask
```

### Run Server (A hello world function can send back real-time on server side to clint, who then shows time on a webpage) 
```bash 
python3 helloworld.py
 * Running on http://0.0.0.0:80/ 
 * Restarting with reloader
 
```
After server app has been launched successfully, you can open a blank webpage and input address "http://0.0.0.0:80" to show demo.

### Run Server (This is a simple webservice to provide CRUD operations to a database.) 
```bash   
python3 WS_Server.py
 * Running on http://0.0.0.0:80/ 
 * Restarting with reloader
 
```

After server app has been launched successfully, you can execute client app to test API functions
```bash   
python3 WS_Client.py 
```



