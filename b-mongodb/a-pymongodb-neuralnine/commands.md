## MongoDB

```sh

(base) ravi0531rp@ravi-MSI:~/Downloads$ sudo systemctl status mongod
○ mongod.service - MongoDB Database Server
     Loaded: loaded (/lib/systemd/system/mongod.service; disabled; vendor preset: enabled)
     Active: inactive (dead)
       Docs: https://docs.mongodb.org/manual
(base) ravi0531rp@ravi-MSI:~/Downloads$ sudo systemctl start mongod
(base) ravi0531rp@ravi-MSI:~/Downloads$ sudo systemctl status mongod
● mongod.service - MongoDB Database Server
     Loaded: loaded (/lib/systemd/system/mongod.service; disabled; vendor preset: enabled)
     Active: active (running) since Tue 2024-02-27 16:46:51 IST; 2s ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 121741 (mongod)
     Memory: 154.4M
        CPU: 246ms
     CGroup: /system.slice/mongod.service
             └─121741 /usr/bin/mongod --config /etc/mongod.conf

Feb 27 16:46:51 ravi-MSI systemd[1]: Started MongoDB Database Server.



```

* Usage
```sh
base) ravi0531rp@ravi-MSI:~/Downloads$ mongosh
Current Mongosh Log ID:	65ddc4f5b59b2eb96ee72ebc
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.5
Using MongoDB:		7.0.5
Using Mongosh:		2.1.5

For mongosh info see: https://docs.mongodb.com/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2024-02-27T16:46:51.763+05:30: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2024-02-27T16:46:51.934+05:30: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2024-02-27T16:46:51.934+05:30: vm.max_map_count is too low
------

test> use mydatabse
switched to db mydatabse
mydatabse> 


```

* Using the Shell
```sh
(base) ravi0531rp@ravi-MSI:~/Downloads$ mongosh
Current Mongosh Log ID:	65ddc4f5b59b2eb96ee72ebc
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.5
Using MongoDB:		7.0.5
Using Mongosh:		2.1.5

For mongosh info see: https://docs.mongodb.com/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2024-02-27T16:46:51.763+05:30: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2024-02-27T16:46:51.934+05:30: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2024-02-27T16:46:51.934+05:30: vm.max_map_count is too low
------

test> use mydatabse
switched to db mydatabse
mydatabse> db.people.insertOne({name : "Ravi", age : 30});
{
  acknowledged: true,
  insertedId: ObjectId('65ddc63db59b2eb96ee72ebd')
}
mydatabse> db.people.find();
[
  { _id: ObjectId('65ddc63db59b2eb96ee72ebd'), name: 'Ravi', age: 30 }
]
mydatabse> db.people.insertOne({name : "Hari", age : 32, interest : ["C++", "Python"]});
{
  acknowledged: true,
  insertedId: ObjectId('65ddc67db59b2eb96ee72ebe')
}
mydatabse> db.people.find();
[
  { _id: ObjectId('65ddc63db59b2eb96ee72ebd'), name: 'Ravi', age: 30 },
  {
    _id: ObjectId('65ddc67db59b2eb96ee72ebe'),
    name: 'Hari',
    age: 32,
    interest: [ 'C++', 'Python' ]
  }
]
mydatabse> 





```

* Codes 
```sh
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

```

```sh
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

```

```sh
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


```