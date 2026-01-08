'''
PyMongo provides methods to update one or many documents in a collection.
'''
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

'''
1. Update One Document (update_one)
Updates the first document that matches the filter.
'''
# Set status to "inactive" for the first matching document
result = collection.update_one(
    {"name": "John"},                  # Filter
    {"$set": {"status": "inactive"}}   # Update operations
)

print(result.matched_count)   # How many documents matched
print(result.modified_count)  # How many were actually modified


'''
2. Update Many Documents (update_many)
Updates all documents that match the filter.
'''
# Add 5 years to age for all users in "New York"
result = collection.update_many(
    {"city": "New York"},
    {"$inc": {"age": 5}}
)

print(result.matched_count)
print(result.modified_count)


'''
Common Update Operators

Operator        Purpose                                Example

$set            Set a field's value                    {"$set": {"status": "active"}}
$unset          Remove a field                         {"$unset": {"old_field": ""}}
$inc            Increment a number                     {"$inc": {"score": 10}}
$mul            Multiply a number                      {"$mul": {"price": 1.1}}
$rename         Rename a field                         {"$rename": {"old": "new"}}
$push           Add to array                           {"$push": {"tags": "python"}}
$addToSet       Add to array if not exists             {"$addToSet": {"tags": "mongodb"}}
$pop            Remove first/last array element        {"$pop": {"tags": -1}} (removes first)
'''

# Set multiple fields
collection.update_one(
    {"email": "user@example.com"},
    {"$set": {"name": "Jane Doe", "updated_at": datetime.utcnow()}}
)


# Upsert (update or insert if not found)
result = collection.update_one(
    {"email": "new@example.com"},
    {"$set": {"name": "New User", "status": "active"}},
    upsert=True
)

if result.upserted_id:
    print("New document inserted with ID:", result.upserted_id)


# Update nested field
collection.update_one(
    {"name": "John"},
    {"$set": {"address.city": "Los Angeles"}}
)


# Update array elements
# Add "admin" to roles array if not present
collection.update_one(
    {"name": "John"},
    {"$addToSet": {"roles": "admin"}}
)

# Increment score for all items in scores array (using $[])
collection.update_many(
    {"scores": {"$exists": True}},
    {"$inc": {"scores.$[]": 5}}
)


# Update with current date
from datetime import datetime

collection.update_many(
    {"status": "active"},
    {"$set": {"last_seen": datetime.utcnow()}}
)


'''
Replace Entire Document (replace_one)
Replaces the whole document (except _id).
'''
new_doc = {"name": "John", "age": 35, "city": "Boston"}

result = collection.replace_one(
    {"name": "John"},
    new_doc
)