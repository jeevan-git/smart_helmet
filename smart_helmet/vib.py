#!/usr/bin/python
import RPi.GPIO as GPIO
import serial
import time, sys

#GPIO Basic Inilizatioin
vib_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(vib_pin, GPIO.IN)

def callback(vib_pin):
        if GPIO.input(vib_pin):
                print ("Movement Detected!")
                sms_func()

def sms_func():
        sms_serial = "/dev/serial0"
	ser = serial.Serial(sms_serial, baudrate=9600, timeout=5)
        ser.write("AT+CMGF=1\r")
        time.sleep(0.5)
        ser.write('AT+CMGS="+9779845699781"\r')
        msg= "Accident has occured "
        ser.write(msg<chr(26))
        time.sleep(0.5)
        print("Message sent")

GPIO.add_event_detect(vib_pin, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(vib_pin, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(0.2)

