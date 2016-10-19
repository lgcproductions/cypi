from gpiozero import Motor
import time

motorr = Motor(forward=22, backward=23)
motorl = Motor(forward=18, backward=17)

while True:
		print "Left motor forward"
		motorl.forward(1)
		time.sleep(0.5)
		motorl.forward(0)
		time.sleep(2)
		
		print "Right motor forward"
		motorr.forward(1)
		time.sleep(0.5)
		motorr.forward(0)
		time.sleep(2)
		
		print "Left motor backwards"
		motorl.backward(1)
		time.sleep(0.5)
		motorl.backward(0)
		time.sleep(2)
		
		print "Right motor backwards"
		motorr.backward(1)
		time.sleep(0.5)
		motorr.backward(0)
		time.sleep(2)
		
	    print "Forward"
        motorl.forward(1)
        motorr.forward(1)
        time.sleep(0.5)
        motorl.forward(0)
        motorr.forward(0)
		time.sleep(2)

        print "Backward"
        motorl.backward(1)
        motorr.backward(1)
        time.sleep(0.5)
        motorl.backward(0)
        motorr.backward(0)
		time.sleep(5)