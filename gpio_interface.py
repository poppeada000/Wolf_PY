#!/usr/bin/env python
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from interface import *
#from gpiozero import Button#Gpio Integration this may be unix operatble
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if __name__ == '__main__':
    pageDiv()
    goHome()
    while True: # Run forever
        if GPIO.input(5) == GPIO.HIGH:
            build(masterQue[0][1])
            pygame.display.update()
            time.sleep(5)
            goHome()
        if GPIO.input(6) == GPIO.HIGH:
            build(masterQue[1][1])
            pygame.display.update()
            time.sleep(5)
            goHome()
        if GPIO.input(13) == GPIO.HIGH:
            build(masterQue[2][1])
            pygame.display.update()
            time.sleep(5)
            goHome()
        if GPIO.input(19) == GPIO.HIGH:
            build(masterQue[3][1])
            pygame.display.update()
            time.sleep(5)
            goHome()
            
#GPIO PINS 5,6,13,19
