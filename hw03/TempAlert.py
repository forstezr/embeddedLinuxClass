#!/usr/bin/env python3
#Zachary Forster CM1646
#ECE434 HW3

import Adafruit_BBIO.GPIO as GPIO
import time
from subprocess import call
import smbus
bus = smbus.SMBus(1)
address_tmp1 = 0x48
address_tmp2 = 0x49

#Run setuo script
GPIO.cleanup()
call("./TempAlertSetup.sh")
bus.write_byte_data(address_tmp1, 1, 0x04)
bus.write_byte_data(address_tmp2, 1, 0x04)



def callBack(ch):
    #interrupt handling for alerts
    if(ch == "P9_12"):
        temp = bus.read_byte_data(address_tmp1, 0)
        print(temp)
        print("its hot")
    elif(ch == "P9_14"):
        temp = bus.read_byte_data(address_tmp2, 0)
        print(temp)
        print("its hot 2")
        



GPIO.setup("P9_12", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_14", GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
GPIO.add_event_detect("P9_12", GPIO.RISING, callback = callBack)
GPIO.add_event_detect("P9_14", GPIO.RISING, callback = callBack)

#set temperature bounds
bus.write_byte_data(address_tmp1, 2, 0x19) #low
bus.write_byte_data(address_tmp1, 3, 0x1a) #high
bus.write_byte_data(address_tmp2, 2, 0x19) #low
bus.write_byte_data(address_tmp2, 3, 0x1a) #high

while(True):
    # temp = bus.read_byte_data(address_tmp1, 0)
    # print(temp)
    # time.sleep(0.2)
    continue

