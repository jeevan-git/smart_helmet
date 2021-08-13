
import RPi.GPIO as GPIO
import serial
import time,sys

#SERIAL_PORT = "/dev/ttyUSB0"
SERIAL_PORT = "/dev/serial0"
ser = serial.Serial(SERIAL_PORT,baudrate = 9600,timeout=5)

ser.write("AT+CMGF=1\r")
print("Text mode enabled...")
time.sleep(3)
ser.write('AT+CMGS="+9779845699781"\r')
msg = "test message from rpi...."
print("sending message...")
time.sleep(3)
ser.write(msg+chr(26))
time.sleep(3)
print("message sent...")
