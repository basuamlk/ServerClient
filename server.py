import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 1234
address = (ip,port)
server.bind(address)
server.listen(1)
print("[*] started listening ",ip,":",port)
client,addr = server.accept()
print("[*] Got a connection from ",addr[0],":",addr[1])
while True:
    data = client.recv(1024)
    print("[*] Received '",data,"' from the client")
    print(" Processing data")
    if(data ==b"Hello server"):
        client.sendall(b"Hello client")
        print(" Processing done.\n[*] Reply sent")
    elif(data == b"disconnect"):
        client.sendall(b"Goodbye")
        client.close()
        break
    else:
        client.sendall(b"Invalid data")
        print(" Processing done Invalid data.\n[*] Reply sent")
