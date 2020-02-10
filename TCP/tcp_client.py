#Veronica Gonzalez
#CPE138 LAB2
#TCP CLIENT
#from socket import *
import socket
#serverName ='raspberrypi'#'127.0.0.1' # 'sp1.ecs.csus.edu'
serverPort = 51202
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.1.1',serverPort))
data = raw_input('Input lowercase sentence:')
#i=0
#for i in range(0,10):
#	i=i+1
clientSocket.send(data.encode())
data_by_server = clientSocket.recv(1024)
print('From Server: ', data_by_server.decode())
clientSocket.close()
