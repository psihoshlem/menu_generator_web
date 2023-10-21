from pymongo import MongoClient

client = MongoClient('mongodb://db:27017')
# client = MongoClient("localhost",27017)

db = client.umom_dishes