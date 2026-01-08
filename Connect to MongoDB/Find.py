# Find One:
'''
In PyMongo (the Python driver for MongoDB), the find_one() method returns a single document matching your query filter (or None if no match is found).
By default, it includes all fields, including the _id field.
'''

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

f = collection.find_one({"name": "Bob"})
print(f)




# Find Many:
'''
To select data from a table in MongoDB, we can also use the find() method.
The find() method returns all occurrences in the selection.
The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.
'''

f_many = collection.find({"city": "Chandausi"})
for doc in f_many:
    print(doc)