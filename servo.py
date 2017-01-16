#!/usr/bin/python
import sys

def main(argv):
	start = argv[1]
	end = argv[2]
	delay = argv[3]
	loop = argv[4]

	import time
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)

	p = GPIO.PWM(11, 100)
	p2 = GPIO.PWM(13, 100)
	p.start(0)
	p2.start(0)
	for i in range(0, int(loop)):
	        for dc in range(int(start), int(end), 1):
        	        p.ChangeDutyCycle(dc)
        	        p2.ChangeDutyCycle(dc)
#        	        print dc
        	        time.sleep(float(delay))

		for dc in range(int(end), int(start), -1):
        	        p.ChangeDutyCycle(dc)
        	        p2.ChangeDutyCycle(dc)
#        	        print dc
        	        time.sleep(float(delay))


	p.stop()
	p2.stop()
	GPIO.cleanup()

if __name__ == "__main__":
	if len(sys.argv) < 5:
		print "servo.py <start> <end> <delay> <loop>"
	else:
		main(sys.argv)
	
