#!/usr/bin/env python3
#Zachary Forster   togglegpio.py

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_12", GPIO.OUT)
def main(sleepTime):
    while True:
        GPIO.output("P9_12", GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output("P9_12", GPIO.LOW)
        time.sleep(sleepTime)
        
main(0.0001)