import socket

client_socket = socket.socket()
host = socket.gethostname()
port = 12345

client_socket.connect((host,port))
print client_socket.recv(1024)
client_socket.close()
