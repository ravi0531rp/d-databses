from pymongo import MongoClient
from bson.objectid import ObjectId

client  = MongoClient(host = 'localhost', port = 27017)

db = client.my_current_db

people = db.people

print([p for p in people.find({"name": "John"})])
print([p for p in people.find({"_id" : ObjectId("65ddcd126ed4937a350edcb3")})])

print([p for p in people.find({"age" : {"$lt" : 25}})]) # age < 25

print(people.count_documents({"name" : "John"})) 

people.update_one({"_id" : ObjectId("65ddcd126ed4937a350edcb3")} , {"$set" : {"age" : 21}}) # update the record


people.delete_many({"age" : {"$lt" : 25}})