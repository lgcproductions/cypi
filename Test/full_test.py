# Code to control cypi. A big thanks to every one's help and their code
# to make this possible.
#
#
#


from gpiozero import LED, Motor
import cwiid, time

motorl = Motor(forward=18, backward=17) #Left Motor
motorr = Motor(forward=22, backward=23) #Right Motor 

triRED = LED(27)
triBLUE = LED(4)
triGREEN = LED(13)


button_delay = 0.1
action_time = 0.2

# Function Definitions

def closeConnection():
  print '\nClosing connection...'
  wii.rumble = 1
  time.sleep(1)
  wii.rumble = 0
  exit(wii)

def moveForwards():
  time.sleep(button_delay)    
  motorl.forward(1)
  motorr.forward(1)
  time.sleep(action_time)
  motorl.stop()
  motorr.stop()

def moveBackwards():
  time.sleep(button_delay)  
  motorl.backward(1)
  motorr.backward(1)
  time.sleep(action_time)
  motorl.stop()
  motorr.stop() 

def turnLeft():
  time.sleep(button_delay)    
  motorr.forward(1)
  time.sleep(action_time)
  motorr.stop()

def turnRight():
  time.sleep(button_delay)    
  motorl.forward(1)
  time.sleep(action_time)
  motorl.stop()


def turnOnRedLed():
  time.sleep(button_delay)
  triRED.on()

def turnOnBlueLed():
  time.sleep(button_delay)
  triBLUE.on()

def turnOnGreenLed():
  time.sleep(button_delay)
  triGREEN.on()

def tunOnAllLeds():
  time.sleep(button_delay)
  triRED.on()
  triBLUE.on()
  triGREEN.on()

def turnOffAllLeds():
  triRED.off()
  triBLUE.off()
  triGREEN.off()

# Function Definitions End



print 'Press 1 + 2 on your Wii Remote now ...'


# Try to connect to the Wiimote & quit if not found
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Can't connect to Wiimote"
  quit()

print 'Wiimote connected'
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
    turnOnRedLed()
		
  elif (buttons & cwiid.BTN_2):
		turnOnBlueLed()

  elif (buttons & cwiid.BTN_1):
    turnOnGreenLed()
		
  elif (buttons & cwiid.BTN_B):
    turnOnAllLeds()
  
  else:
    turnOffAllLeds()

