import web
import pymongo
import json


#calls index method only if url in format /'some character string' --only accepts characters
urls= ( '/(\w+)', 'index')

class index:

	def GET(self, room_name):
		#connect to mongodb
		from pymongo import MongoClient
		client = MongoClient('mongodb://admin:admin0@ds145405.mlab.com:45405/breakthebuild?authMechanism=SCRAM-SHA-1')
		db = client['breakthebuild']
		collection = db.test_collection
			
		ret_val = collection.find_one({'name': room_name})		

		#check if a value was returned, else will error out when trying to read hash
		if ret_val:
			if ret_val["occupied"] == False:
				return "Free\n"
		else:
			return "Occupied\n"
		

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

web.config.debug = False

