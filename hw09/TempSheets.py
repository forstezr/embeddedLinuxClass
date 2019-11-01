#!/usr/bin/env python3
#Zachary Forster CM1646
#ECE434 
#This program only reads i2c data from the tmp101.


import Adafruit_BBIO.GPIO as GPIO
import time
from subprocess import call
import smbus
bus = smbus.SMBus(2)

address_tmp2 = 0x49

while(True):
    temp = bus.read_byte_data(address_tmp2, 0)
    print(temp)
    time.sleep(0.2)
    #continue
