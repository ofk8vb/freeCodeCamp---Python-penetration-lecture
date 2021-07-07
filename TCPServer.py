import socket

serversocket = socket.socket(
    socket.AF_INET, # means we are using ipv4
    socket.SOCK_STREAM
)

host = socket.gethostname() # it will get host name (local machine) returns ip address in string format
port = 444 # can be whatever you want

serversocket.bind((host,port)) # bind the addresses we specified to our socket object 

serversocket.listen(3) # how many requests to allow at the same time

while True:
    clientsocket, address = serversocket.accept() #clientsocket will be used to communicate with the client
    
    print('received connection from: %s ' % str(address))
    message = 'Hello! Thank you for connecting to the server. This is an example of how sockets can be used' + '\r\n'
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()


