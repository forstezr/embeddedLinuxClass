#!/usr/bin/env python3
#Zachary Forster CM1646
#ECE434 HW2

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.cleanup()

def call(channel):
    if GPIO.input(channel):
        if channel == "P9_21":
            GPIO.output("P9_11", GPIO.HIGH)
        elif channel == "P9_16":
            GPIO.output("P9_12", GPIO.HIGH)
        elif channel == "P9_17":
            GPIO.output("P9_13", GPIO.HIGH)
        elif channel == "P9_18":
            GPIO.output("P9_14", GPIO.HIGH)
    else:
        if channel == "P9_21":
            GPIO.output("P9_11", GPIO.LOW)
        elif channel == "P9_16":
            GPIO.output("P9_12", GPIO.LOW)
        elif channel == "P9_17":
            GPIO.output("P9_13", GPIO.LOW)
        elif channel == "P9_18":
            GPIO.output("P9_14", GPIO.LOW)
    
    
def main():
    GPIO.setup("P9_11", GPIO.OUT)
    GPIO.setup("P9_12", GPIO.OUT)
    GPIO.setup("P9_13", GPIO.OUT)
    GPIO.setup("P9_14", GPIO.OUT)
    
    GPIO.setup("P9_21", GPIO.IN)
    GPIO.setup("P9_16", GPIO.IN)
    GPIO.setup("P9_17", GPIO.IN)
    GPIO.setup("P9_18", GPIO.IN)
        
    GPIO.add_event_detect("P9_21", GPIO.BOTH, callback = call)
    GPIO.add_event_detect("P9_16", GPIO.BOTH, callback = call)
    GPIO.add_event_detect("P9_17", GPIO.BOTH, callback = call)
    GPIO.add_event_detect("P9_18", GPIO.BOTH, callback = call)
    
    try:
        while True:
            continue
    except KeyboardInterrupt:
        GPIO.cleanup()
        
if __name__ == "__main__":
    main()