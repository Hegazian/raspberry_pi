import RPI.GPIO as GPIO

GPIO.setmde(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)


def forward():
	GPIO.output(7,True)
	GPIO.output(8,False)
	GPIO.output(9,True)
	GPIO.output(10,False)

def back():
	GPIO.output(7,False)
	GPIO.output(8,True)
	GPIO.output(9,False)
	GPIO.output(10,True)

def right():
	GPIO.output(7,True)
	GPIO.output(8,False)
	GPIO.output(9,False)
	GPIO.output(10,True)	

def left():
	GPIO.output(7,False)
	GPIO.output(8,True)
	GPIO.output(9,True)
	GPIO.output(10,False)

