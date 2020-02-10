#Veronica Gonzalez
#UDP PINGER CLIENT

from socket import *
serverName = 'sp1.ecs.csus.edu'

#Port number
serverPort = 12048
import time

#create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
timeout = clientSocket.settimeout(1)
time_start = time.time()
sequence_number = 0
while sequence_number<10:
	sequence_number += 1
	try: 
		message = ('ping'+ str(sequence_number) + time.time())
		clientSocket.sendto(message.encode(),(serverName, serverPort))
		modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
		print(modifiedMessage.decode())
		time_end = time.time()-time_start
		print('sequence number: '+ sequence_number)
		print ('RTT= '+time_end)
		print 'seconds'

	except:
		print('request timed out')
		clientSocket.close()

clientSocket.close()
