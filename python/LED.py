#!/usr/bin/python

import time
import mraa

LED_PIN = 6
led = mraa.Gpio(LED_PIN)
led.dir(mraa.DIR_OUT)

def turnOnLED():
    led.write(1)

def turnOffLED():
    led.write(0)

def ledStatus():
    return led.read()

def reverseLED():
    if ledStatus() == 1:
        turnOffLED()
    else:
        turnOnLED()

def blinkOnce():
    turnOnLED()
    time.sleep()
    reverseLED()

def blinkLoop():
    while 1:
        reverseLED()
        time.sleep(1)

if __name__=="__main__":
    blinkLoop()
