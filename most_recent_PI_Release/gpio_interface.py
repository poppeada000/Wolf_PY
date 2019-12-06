#!/usr/bin/python
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from interface import *
#from gpiozero import Button#Gpio Integration this may be unix operatble
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
timerStart = time.time()

def button_pushed(page):
    for i in masterQue[page][1]:
        build(i)
    pygame.display.update()
    delay = 0
    timeout = time.time() + 10
    print(time.time())
    while(True):
        if(time.time() > timeout):
            break
        if GPIO.input(5) == GPIO.LOW:
            newpage()
            button_pushed(0)
        if GPIO.input(6) == GPIO.LOW:
            newpage()
            button_pushed(1)
        if GPIO.input(13) == GPIO.LOW:
            newpage()
            button_pushed(2)
        if GPIO.input(19) == GPIO.LOW:
            newpage()
            button_pushed(3)
        if GPIO.input(26) == GPIO.LOW:
            break


def check_for_push():
    while True: # Run forever
        if GPIO.input(5) == GPIO.LOW:
            newpage()
            button_pushed(0)
            goHome()
        if GPIO.input(6) == GPIO.LOW:
            newpage()
            button_pushed(1)
            goHome()
        if GPIO.input(13) == GPIO.LOW:
            newpage()
            button_pushed(2)
            goHome()
        if GPIO.input(19) == GPIO.LOW:
            newpage()
            button_pushed(3)
            goHome()
        if GPIO.input(26) == GPIO.LOW:
            done()
            break
        
        
if __name__ == '__main__':
    pageDiv()
    goHome()
    check_for_push()
    #GPIO PINS 5,6,13,19
