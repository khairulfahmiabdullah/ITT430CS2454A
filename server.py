#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.47.132' # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

while True:
   print 'Waiting for connection from Client'
   c, addr = s.accept()     # Establish connection with client.
   print 'Connection Established from', addr
   c.send('Thank you for connecting to Python Socket Server')
   c.close()                # Close the connection
   
