from pymongo import MongoClient
from bson.son import SON

client = MongoClient('localhost', port=27017)

db = client.my_current_db

people = db.people

people.insert_one({"name": "Sourav", "age": 26, "interests": ["C++", "Python"]})
people.insert_one({"name": "Shalu", "age": 25, "interests": ["JS", "Python"]})
people.insert_one({"name": "Shalu", "age": 25})


pipeline = [
    {
        "$group" : {
            "_id": "$name",
            "average_age": {"$avg" : "$age"},
        }
    },
    {
        "$sort" : SON([("average_age", -1), ("_id", -1)])
    }
]

result = people.aggregate(pipeline)

for res in result:
    print(res)