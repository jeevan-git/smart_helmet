import RPi.GPIO as GPIO
import serial
import time,sys
SERIAL_PORT = "/dev/ttyS0"
ser = serial.Serial(SERIAL_PORT,baudrate = 9600,timeout=5)
ser.write("ATD9845699781;\r")
print("DIALLING")
time.sleep(10)
ser.write("ATH\r")
print("hanging up")
