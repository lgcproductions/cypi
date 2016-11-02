#!/usr/bin/python
#Main file for Cypi, a Raspbery Pi based Cybot.	#
#												#
#V1.0											#
#Thank's to all that have helped with this code	#
#################################################

import cwiid, time
from RPi import GPIO
from gpiozero import Motor
from cyled import *
from cyscreen import *

'''

Set up the pins for all the connected sensors

'''
#Sonar pins

TRIGL = 12 #left sonar
ECHOL = 16 #left sonar

TRIGR = 20 #right sonar
ECHOR = 21 #right sonar

#Light Dependent Resistor
LDRl = 5
LDRr = 6

#Pin assingment for the left and right motors. 
motorr = Motor(forward=22, backward=23) #Right moror
motorl = Motor(forward=18, backward=17) #Left Motor

action_time = 0.2 #timer for the motor definitions


#delay for wii remote buttons
button_delay = 0.1


'''
Next section is for all the definitions used within the main program

'''
#-------------START OF DEFINITIONS-----------#

#Definitions used by the wii remote

def closeConnection():
  print '\nClosing connection...'
  wii.rumble = 1
  time.sleep(1)
  wii.rumble = 0
  screnClear()
  exit(wii)

#Definitions for the motors
def moveForwards():
  motorl.forward(1)
  motorr.forward(1)
  time.sleep(action_time)
  motorl.stop()
  motorr.stop()

def moveBackwards():
  motorl.backward(1)
  motorr.backward(1)
  time.sleep(action_time)
  motorl.stop()
  motorr.stop() 

def turnLeft():
  motorr.forward(1)
  time.sleep(action_time)
  motorr.stop()

def turnRight():
  motorl.forward(1)
  time.sleep(action_time)
  motorl.stop()

  
  
# Definitions for the sonar sensors, left and right. 
 
def sonarr():
	#set the in/output mode of the pins
	GPIO.setup(TRIGR,GPIO.OUT)
	GPIO.setup(ECHOR,GPIO.IN)

	GPIO.output(TRIGR, False)
	time.sleep(0.02) #wait for sensor to settle
	GPIO.output(TRIGR, True)
	time.sleep(0.00001)
	GPIO.output(TRIGR, False)
	
	while GPIO.input(ECHOR)==0:
		pulse_start = time.time()

	while GPIO.input(ECHOR)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)
	
	return distance
	
def sonarl():
	#set the in/output mode of the pins
	GPIO.setup(TRIGL,GPIO.OUT)
	GPIO.setup(ECHOL,GPIO.IN)

	GPIO.output(TRIGL, False)
	time.sleep(0.02) #wait for sensor to settle
	GPIO.output(TRIGL, True)
	time.sleep(0.00001)
	GPIO.output(TRIGL, False)
	
	while GPIO.input(ECHOL)==0:
		pulse_start = time.time()

	while GPIO.input(ECHOL)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)
	
	return distance
 
#Definitions used by the light sensors 

def ldrl ():
        reading = 0
        GPIO.setup(LDRl, GPIO.OUT)
        GPIO.output(LDRl, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(LDRl, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(LDRl) == GPIO.LOW):
                reading += 1
        return reading

def ldrr ():
        reading = 0
        GPIO.setup(LDRr, GPIO.OUT)
        GPIO.output(LDRr, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(LDRr, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(LDRr) == GPIO.LOW):
                reading += 1
        return reading  
 
#definitions for the sonar avoider

def avoider():
	while True:
		if (sonarl() <=10)and(sonarr() <=10):
			print 'backward'
			moveBackwards()
		
		elif (sonarl() <=8):
			print 'turn right'
			turnRight()
		
		elif (sonarr() <=8):
			print 'turn left'
			turnLeft()
		elif (buttons & cwiid.BTN_B):
			break
		
		else:
			print 'forward'
			moveForwards()
			
#definitions for the light follower

def lightFollower():
	while True:
		if (ldrl() <=1100):
			print 'turn right'
			turnRight()
		
		elif (ldrr() <=1100):
			print 'turn left'
			turnLeft()	
		elif (buttons & cwiid.BTN_B):
			rgbexcited(2)
			
		else:
			print 'forward'
			moveForwards()

 
#-------------END OF DEFINITIONS-----------#
 
'''
Below is the main section of the program

'''
#-------------MAIM CODE-----------#

screenLogo()
time.sleep(3)
rgbshocked(3)  

print 'Press 1 + 2 on your Wii Remote now ...'
screenWiiconnect()
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  screenWiierror()
  quit()

print 'Wii Remote connected...\n'
screenConnected()
wii.rpt_mode = cwiid.RPT_BTN
 
while True:
  buttons = wii.state['buttons']

  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    closeConnection()

  elif (buttons & cwiid.BTN_UP):
    moveForwards()

  elif (buttons & cwiid.BTN_DOWN):
    moveBackwards()
  
  elif (buttons & cwiid.BTN_LEFT):
    turnLeft()
   
  elif(buttons & cwiid.BTN_RIGHT):
    turnRight()
	
  elif (buttons & cwiid.BTN_A):
    VegasMode()
   
  elif(buttons & cwiid.BTN_1):
    lightFollower()
	
  elif (buttons & cwiid.BTN_2):
    avoider()	
	
  else:
    rgbexcited(0)
