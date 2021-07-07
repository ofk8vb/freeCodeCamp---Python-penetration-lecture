import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.2.213'
host = socket.gethostname()

port = 444

clientsocket.connect(('192.168.2.213',port))

# get the message sent back by the server
message = clientsocket.recv(1024) # memory allocated for receiving

clientsocket.close()

# message sent back by the server is encoded in ascii
print(message.decode('ascii'))