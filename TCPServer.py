#!/usr/bin/python3

import socket

# Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.1.107'
host = socket.gethostbyname()
port = 444

# Binding to socket
serversocket.bind(('192.168.1.107', port)) # host will be replaced/substituted with IP, if changed and not running on host

# Starting TCP listener
serversocket.listen(3)

while True:
    # Starting the connection
    clientsocket, address = serversocket.accept()
    
    print("received connection from %s " % str(address))
    
    message = 'Hello! Thank you for connecting to the server' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()
