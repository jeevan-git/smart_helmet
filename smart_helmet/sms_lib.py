#!/usr/bin/python
from pynmea2.nmea_utils import LatLonFix
import RPi.GPIO as GPIO
from sim800l import SIM800L
from time import sleep

import time
import serial
import string
import pynmea2

global Flag
global alc_Flag
global switch_Flag
global vib_Flag
global gps_Flag
global lat
global lng

Flag = True

alc_pin = 20	
vib_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(vib_pin, GPIO.IN)
GPIO.setup(alc_pin, GPIO.IN)

def sms_send():
    global Flag
    sms_serial = "/dev/serial0"
    SMS_serial = SIM800L(sms_serial)
    acc_msg = "Accident has ocurred at place with latittude =" + str(lat) + "and longitude =" +str(lng)
    SMS_serial.send_sms('+9779845699781', acc_msg)
    print("SMS sent succesfully")
    Flag = False

def vib_sensor(vib_pin):
    if GPIO.input(vib_pin):
        vib_Flag = True

def alc_sensor():
    while(count<20):
    input_air = GPIO.input(alc_pin)
    if(input_air):
        alc_Flag = False
    else:
        alc_Flag = True
    print(alc_Flag)
    cout=cout+1
    sleep(0.2)

def gps_sensor():

    port="/dev/ttyUSB0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata=ser.readline()
    if newdata[0:6] == "$GPRMC":
        newmsg=pynmea2.parse(newdata)
        lat=newmsg.latitude
        lng=newmsg.longitude
        gps_Flag = True
        # gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
        # print(gps)

def blu_sensor():
    if(switch_Flag==True and )
    blu_Flag = True


GPIO.add_event_detect(vib_pin, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(vib_pin, vib_sensor)


# infinite loop
while Flag:
    time.sleep(0.2)
