import wiringpi as wiringpi
from time import sleep

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, 0)
count=0
while(count<20):
	my_input=wiringpi.digitalRead(18)
	if(my_input):
		print("Not Detected !")
	else:
		print("Alcohol Detected")
	count=count+1
	sleep(1)