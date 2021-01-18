# CLIENT B
import socket 
#create socket tcp
s = socket.socket()
#server instance IP address
serverip  = "192.168.43.237"
#server port used in server program
serverport = 2221

#connect to the server program
s.connect((serverip, serverport))

# recieve msg from server
print(s.recv(100))

#send msg to server
s.send(b'I M client B')