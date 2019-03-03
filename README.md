# ServerClient
This script creates a server and displays how a client and server connect and how they interact,
Sending a greeting message to the server (b'Hello server') and receiving a message back (b'Hello client').
Server will disconnect if client sends message (b'disconnect'). 
### Run the Server:
### Takes in 3 Commands: Script Name, IP, Server PORT (1234):
```
server.py 69.89.31.226 1234
```



### For Client:
```>>> socket.gethostname()
>>> socket.gethostname()
'Computer Name Here'
>>> socket.gethostbyname('Computer Name Here')
'Your IP'
>>> client.connect(('Your IP',1234))
>>> client.sendall(b'Hello server')
>>> client.recv(1024)
b'Hello client'
```
