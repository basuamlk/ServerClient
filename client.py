import socket

### For Client:
name = socket.gethostname()
ip = socket.gethostbyname(name)
client = socket.socket()
client.connect((ip,1234))
client.sendall(b'Hello server')
print('Response from server:')
print('\n>>>',client.recv(1024))
input("\nPress enter key to exit...")