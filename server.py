import socket, threading

# by default args is tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#create & resuse same socket, server already connected error is also fixed.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

port = 2221

#empty means any ip 0.0.0.0
ip = ""

s.bind((ip,port))
s.listen()

#massenger sends and recieves from server and client resp.
def massenger(csession, addr):
    print(addr)
    csession.send(b'I m server')
    #100 capacity of buffer
    data = csession.recv(100)
    print(data)

# create new thread only when client increases and start
while True:
    csession,addr=s.accept()
    t1 = threading.Thread(target=massenger, args=(csession, addr))
    t1.start()
