from pymongo import MongoClient
import datetime
from gpiozero import MotionSensor
import time

temp_readings = 0

def active_count():
	global temp_readings 
	temp_readings += 1
	print("increasing count")

def active_count_reset():
	global temp_readings 
	temp_readings = 0
	print("resetting count")

client = MongoClient("mongodb://admin:admin0@ds145405.mlab.com:45405/breakthebuild?authMechanism=SCRAM-SHA-1")

db = client["breakthebuild"]

test_collection = db.test_collection


sensor = MotionSensor(4,5,2,0.5,False)

last = datetime.datetime.utcnow()

while True:
	if datetime.datetime.utcnow() > last + datetime.timedelta(seconds = 10):
		print(temp_readings)
		if temp_readings > 5:
			occupied = True
		else: 
			occupied = False
		
		test_collection.insert({
			"name" : "Lilly",
			"location" : "3.L",
			"occupied" : occupied,
			"timestamp" : datetime.datetime.utcnow()
			})
		temp_readings = 0
		last = datetime.datetime.utcnow()
					
	sensor.wait_for_motion(60)
	time.sleep(2)
	temp_readings += 1
	print("fired or timeout") 
