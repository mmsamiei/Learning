import socket

client_socket = socket.socket()
host = socket.gethostname()
port = 1376

#client_socket.connect((host,port))
client_socket.connect(('37.59.145.129',port))
print client_socket.recv(1024)
client_socket.close()

