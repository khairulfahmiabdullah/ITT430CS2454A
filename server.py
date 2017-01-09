import RPi.GPIO as GPIO
import time
import socket
import sys

s        = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host     = '192.168.137.10'
port     = 22226
x        = 'Motion Detected! Something caught in the mousetrap'

PIR_PIN  = 7
PIR_PIN2 = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(PIR_PIN2, GPIO.OUT)
pwm = GPIO.PWM(PIR_PIN2, 50)
pwm.start(5)

angle1 = 10
duty1  = float(angle1)/10

s.bind((host,port))
s.listen(5)


while 1:
	c, addr  = s.accept()
	print 'Client Connected'

	def MOTION(PIR_PIN):
	 c.send(x)
	 print x
	 pwm.ChangeDutyCycle(duty1)
     time.sleep(3)
	 pwm.start(5)
	 c.send('Bye-bye.. Thanks for Connecting')
	 time.sleep(2)
	 GPIO.cleanup()
     sys.exit(0)
	 
	 

	while True:
		data = c.recv(1024).decode()
		print 'Client :' + data + '\n'

		if data == 'start':
		 c.send("Waiting for captured")
		 GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION) 
		 while 1:
		   time.sleep(0.5)
		 
		else:
		  GPIO.cleanup()
		  c.close()
	else:
	 s.close()
