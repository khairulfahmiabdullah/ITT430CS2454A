#!/usr/bin/python # This is server.py file
import socket # Import socket module
import RPi.GPIO as GPIO
import time

s = socket.socket() # Create a socket
host = socket.gethostname() # Get local machine name 
port = 12345 # 
s.bind((host, port)) # Bind to the port 
s.listen(5) # Now wait for client connection. 
while True:
   print 'Waiting for connection from Client'
   c, addr = s.accept() # Establish connection with client.
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False) 
   GPIO.setup(23,GPIO.OUT) 
   GPIO.output(23,GPIO.HIGH)
   time.sleep(10)#onlyfor10sec
   GPIO.output(23,GPIO.LOW)
   print 'Connection Established from', addr
   c.send('Thank you for connecting to Python Socket Server')
   c.close() # Close the connection
   

