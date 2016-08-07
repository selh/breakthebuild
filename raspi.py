import pymongo import MongoClient
import datetime

client = MongoClient( mongodb://admin:admin0@ds145405.mlab.com:45405)

db = client['breakthebuild']

test_collection = db.test_collection

test_entry = { "author" : "Janik Andreas",
			"value" : 1,
			"timestamp" : datetime.datetime.utcnow()}

test_collection.insert_one()