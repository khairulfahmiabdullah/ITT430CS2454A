#!/usr/bin/python           # Client.py file

import socket
import time
import sys

x=1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
host = 'localhost' 
port = 22226

s.connect((host, port))
print "Enter 'start' to begin the process : "
while True:
	l = raw_input()
	s.send(l)
 	for x in range (0, 3):
		time.sleep(1)
		data = s.recv(1024).decode()
		print "Server : " + data

	else:
	 sys.exit(0)		
s.close()                    

