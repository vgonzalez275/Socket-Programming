#Veronica Gonzalez
#TCP CLIENT

import socket

#serverName ='raspberrypi'#'127.0.0.1' # 'sp1.ecs.csus.edu'
serverPort = 51202
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.1.1',serverPort))
data = raw_input('Input lowercase sentence:')


clientSocket.send(data.encode())
data_by_server = clientSocket.recv(1024)
print('From Server: ', data_by_server.decode())
clientSocket.close()
