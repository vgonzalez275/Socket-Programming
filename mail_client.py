#Veronica Gonzalez
#CPE 138 PLab2 
#SMTP mail client

from socket import * 

msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n" 

# Choose a mail server (e.g. Google mail server) and call it mailserver  
mailserver = 'smtp.gmail.com'#'mail.smtp2go.com'
port = 587#2525 #port 465 for SSL or 587 for TLS

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port)) 
recv = clientSocket.recv(1024).decode() 
print(recv) 
if recv[:3] != '220':  
	print('220 reply not received from server.') 
 
# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode()) 
recv1 = clientSocket.recv(1024).decode() 
print(recv1) 
if recv1[:3] != '250':     
	print('HELO 250 reply not received from server.') 

#start ttls
#start_ttls = 'startttls\r\n'
#clientSocket.send(start_ttls.encode()) 
#recv_ttls = clientSocket.recv(1024).decode()
#print(recv_ttls)

# Send MAIL FROM command and print server response.  
mail_from_command = 'MAIL FROM: <vgonzalez275@gmail.com> \r\n'
clientSocket.send(mail_from_command.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
#reply not received 
if recv2[:3] != '250':     
	print('MAIL 250 reply not received from server.')

# Send RCPT TO  
rcpt_to_command = 'RCPT TO: <vgonzalez275@gmail.com> \r\n'
clientSocket.send(rcpt_to_command.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':     
	print('RCPT 250 reply not received from server.')

# Send DATA command and print server response.   
DATA_Command = 'DATA\r\n'
clientSocket.send(DATA_Command.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':     
	print('DATA 354 reply not received from server.')

# Send message data. 
clientSocket.send(msg+endmsg)
# Message ends with a single period. 
clientSocket.send(msg+endmsg)
# Send QUIT command and get server response. 
quit_cmd = 'QUIT\r\n'
clientSocket.send(quit_cmd.encode())
recv5 =  clientSocket.recv(1024).decode()
print(recv5)
if recv4[:3] != '221':     
	print('Error on Quit')

clientSocket.close() 

#CPE151 Notes
#power,delay,dynamic circuit,layout, adders, different kinds of adders, using p,g,k, mirror architecture adders, comparators, circuit testing--> given a sequence, how do you find the fault, given hold time, etc. how to write sram, what are the combined requiremnts do design sram, dram. combinational circuit give the propagation and other one 
