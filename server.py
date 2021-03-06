import web
import pymongo


#calls meeting_rooms method only if url in format /'some character string'
urls= ( '/meeting_rooms/(\w+)', 'meeting_rooms')

class meeting_rooms:

	def GET(self, room_name):
		#connect to mongodb
		from pymongo import MongoClient
		client = MongoClient('mongodb://admin:admin0@ds145405.mlab.com:45405/breakthebuild?authMechanism=SCRAM-SHA-1')
		db = client['breakthebuild']
		collection = db.test_collection
			
		ret_val = collection.find_one({"name": room_name})		
	
		#check if a value was returned, else will error out when trying to read hash
		if ret_val:
			if ret_val["occupied"] == False:
				return { 
					 "status" : "Free"
                  		        }
			else:
				return {
					"status" : "Occupied"
					}

		else:
			return { 
                                "status" : "Occupied"
                               }

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

web.config.debug = False
