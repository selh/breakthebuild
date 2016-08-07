#cool python file
#Authors: Happy Hour Squad

from gpiozero import MotionSensor
import time

#pir = MotionSensor(pin=4,queue_len=10,sample_rate=1.0,threshold=0.5,partial=False)
pir2 = MotionSensor(4) 

def abc():
	print("Motion detected")

pir2.when_motion = abc

while True:
	#if pir2.motion_detected:
		#print("Motion detected!")
	a = 3
