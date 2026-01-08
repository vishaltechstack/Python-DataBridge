'''
PyMongo provides several methods to delete documents from a collection.
'''
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

'''
1. Delete One Document (delete_one)
Deletes the first document that matches the filter.
'''
# Delete one document where name = "John"
result = collection.delete_one({"name": "John"})

print(result.deleted_count)


'''
2. Delete Many Documents (delete_many)
Deletes all documents that match the filter.
'''
# Delete all documents where status = "inactive"
result = collection.delete_many({"status": "inactive"})

print(result.deleted_count)


'''
3. Delete All Documents in Collection
'''
# Delete everything
result = collection.delete_many({})  # Empty filter matches all

print(result.deleted_count)


'''
4. Common Examples
    • Delete by ObjectId
'''
from bson import ObjectId

object_id = ObjectId("507f1f77bcf86cd799439011")
result = collection.delete_one({"_id": object_id})

print(result.deleted_count)


# • Delete with complex query
result = collection.delete_many({
    "age": {"$gt": 60},
    "city": "New York"
})

print(result.deleted_count)


# • Delete if exists (safe check)
result = collection.delete_one({"email": "user@example.com"})
if result.deleted_count == 1:
    print("Document deleted successfully")
else:
    print("No document found to delete")