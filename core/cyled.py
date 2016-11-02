#!/usr/bin/python
#LED file for Cypi. 							#
#Quick and easy to add or change the behaviour	#
#of the LED's 									#
#V1.0											#
#Thank's to all that have helped with this code	#
#################################################
from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=4, green=27, blue=13)


	
def VegasMode():
    rgbhappy(1)
    rgbexcited(1)
    rgbwarning(1)
    rgbshocked(1)
    rgbanger(1)
    rgbconnecting(1)

def rgbhappy(y):
	n = 3
	while n > 0:
		led.blink(2, 1, 0.5, 0.5, (1, 0 , 1), (0, 0 ,0), y)
		sleep(y)
		n -= 1
		
	else:
		led.off()
		
def rgbexcited(y):
	n = 2
	while n > 0:
		led.blink(0.5, 0.5, 0.5, 0.5, (1, 0 , 1), (0, 0 ,0), y)
		sleep(y)
		n -= 1
		
	else:
		led.off()
	
def rgbwarning(y):
	n = 5
	while n > 0:
		led.blink(1, 1, 0.5, 0.5, (1, 0 , 0), (1, 0.2, 0), y)
		sleep(y)
		n -= 1
		
	else:
		led.off()
	
def rgbshocked(y):
	n = 2
	if n > 0:
		led.blink(0.2, 0.2, 0, 0, (0, 0 , 1), (0, 0, 0), y)
		n -= 1
	elif n == 0:
		led.off()
	
def rgbanger(y):
	count = 5
	while count > 0:
		led.blink(0.5, 0.2, 0.2, 0.2, (0.2, 0, 0), (1, 0, 0), y)
		sleep(y)
		count = count - 1
	else:
		led.off()

def rgbconnecting(y): #this needs to be finalized.
	n = 2
	if n > 0:
		led.blink(0.2, 0.2, 0, 0, (0, 0 , 1), (0, 0, 0), y)
		n -= 1
	elif n == 0:
		led.off()
		
def blue():
	led.blue = 1  # full blue
	sleep(0.5)
	led.blue = 0
	
def red():
	led.red = 1  # full red
	sleep(0.5)
	led.red = 0
	
def green():
	led.green = 1  # full green
	sleep(0.5)
	led.green = 0
	
def white():
	green()
	red()
	blue()
	
