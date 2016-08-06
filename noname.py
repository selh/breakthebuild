#cool python file
#Authors: Happy Hour Squad

from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
	if pir.motion_detected:
		print("Motion detected!")
