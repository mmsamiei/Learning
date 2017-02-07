import socket
import time

server_socket = socket.socket()
host = socket.gethostname()
port = 12345
server_socket.bind((host,port))

server_socket.listen(5)
while True:
    chanal, address = server_socket.accept()
    print 'Get Connection from:{addr}'.format(addr=address)
    str_time = time.ctime()
    chanal.send('{time}'.format(time=str_time))
    chanal.close()
