from pymongo import MongoClient
import pandas as pd

client = MongoClient("localhost", 27017)

db = client.my_current_db # refer to a db, it may/ may not exist

people = db.people # refer to collection named people

people.insert_one({"name": "John", "age": 30})
people.insert_one({"name": "John", "age": 30}) # it will add a new item with new ID
lisa_id = people.insert_one({"name": "Lisa", "age": 34, "interest" : [1, 2, 3]}) # it runs the operation and returns the ID as well
for person in people.find():
    print(person)