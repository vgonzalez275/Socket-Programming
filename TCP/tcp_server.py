#Veronica Gonzalez
#CPE138 LAB2
#TCP SERVER
#from socket import *
import socket

serverPort = 80
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serverSocket.bind(('', 4digit)) for socket visible within the same machine

#socket can be visible to outside world
host = socket.gethostname()
serverSocket.bind((host, serverPort))

#queue up to 5 connect requests
serverSocket.listen(5)
print('The server is ready to receive')

while True:
	#accept connections from outside
	clientSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = sentence.upper()
	clientSocket.send(capitalizedSentence.encode())
	clientSocket.close()
