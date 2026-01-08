# Insert one:
'''
To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.
'''
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

document = {"name": "Mohit", "city": "Chandausi"}
result = collection.insert_one(document)
print("Inserted ID:", result.inserted_id)



# Insert many:
'''
To insert multiple documents into a collection in MongoDB, we use the insert_many() method.
The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert:
'''
documents = [
    {"name": "Alice", "age": 25, "city": "Delhi"},
    {"name": "Bob", "age": 30, "city": "Mumbai"},
    {"name": "Charlie", "age": 35, "city": "Bangalore"}
]

result = collection.insert_many(documents)
print("Inserted IDs:", result.inserted_ids)