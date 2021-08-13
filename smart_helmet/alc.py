import RPi.GPIO as GPIO

from time import sleep
alc_pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(alc_pin, GPIO.IN)

count=0
while(count<20):
	my_input=GPIO.input(alc_pin):
	if(my_input):
		print("Not Detected !")
	else:
		print("Alcohol Detected")
	count=count+1
	sleep(1)