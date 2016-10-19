# Code to control cypi. A big thanks to every one's help and there code
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
  if (buttons & cwiid.BTN_UP):
    #Forwards
    time.sleep(button_delay)    
    motorl.forward(1)
    motorr.forward(1)
    time.sleep(0.2)
    motorl.stop()
    motorr.stop()

  elif (buttons & cwiid.BTN_DOWN):
    time.sleep(button_delay)  
    motorl.backward(1)
    motorr.backward(1)
    time.sleep(0.2)
    motorl.stop()
    motorr.stop()

  
  elif (buttons & cwiid.BTN_LEFT):
    time.sleep(button_delay)         
    motorr.forward(1)
    time.sleep(0.2)
    motorr.stop()

   
  elif(buttons & cwiid.BTN_RIGHT):
    time.sleep(button_delay)          
    motorl.forward(1)
    time.sleep(0.2)
    motorl.stop()
    
  elif (buttons & cwiid.BTN_A):
	time.sleep(button_delay)
	triRED.on()
		
  elif (buttons & cwiid.BTN_2):
	time.sleep(button_delay)
	triBLUE.on()
		
  elif (buttons & cwiid.BTN_1):
	time.sleep(button_delay)
	triGREEN.on()
		
  elif (buttons & cwiid.BTN_B):
	time.sleep(button_delay)
	triRED.on()
	triBLUE.on()
	triGREEN.on()
  
  else:
    triRED.off()
	triBLUE.off()
	triGREEN.off()
   

    
#press button A to stop all motors
  if (buttons & cwiid.BTN_A - cwiid.BTN_B):
    time.sleep(button_delay)          
     

  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)







