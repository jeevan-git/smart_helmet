from sim800l import SIM800L
sim800l=SIM800L('/dev/ttyUSB0')

sms = 'Hello there'
sim800l.send_sms('+9779845699781',sms)
