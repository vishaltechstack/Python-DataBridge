# Creating a collection

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]  # Collection created here (lazily on first insert)


# Checking if the collection exists

# Example: 1
print(db.list_collection_names())   # Lists all collection names in the database

# Example: 2
collist = db.list_collection_names()
if "mycollection" in collist:
    print("The collection exists.")