#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


def main():

    print "executing script"
    pin = 14
    # tell the GPIO module that we want 
    # to use the chip's pin numbering scheme
    GPIO.setmode(GPIO.BCM)
    # setup pin 5 as an output
    GPIO.setup(pin,GPIO.OUT)

    # turn pin on 
    GPIO.output(pin,True)
    # sleep for 3 seconds
    time.sleep(60)
    # turn the pin off
    GPIO.output(pin,False)

    GPIO.cleanup()

if __name__=="__main__":
    main()
