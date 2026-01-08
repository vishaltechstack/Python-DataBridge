# Basic Setup

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")  # Or connect to your MongoDB instance
db = client["your_database"]
collection = db["your_collection"]

'''
Finding Documents
    • find_one(): Returns the first matching document (or None).
    • find(): Returns a cursor to iterate over matching documents.
'''

# Equality Match
# Find one document where name = "Bob"
doc = collection.find_one({"name": "Bob"})
print(doc)

# Find all
for doc in collection.find({"name": "Bob"}):
    print(doc)


'''
Comparison Operators
Common operators: 
    • $eq 
    • $gt 
    • $gte 
    • $lt 
    • $lte 
    • $ne 
    • $in 
    • $nin
'''

# Age greater than 30
for doc in collection.find({"age": {"$gt": 30}}):
    print(doc)

# Status in ["active", "pending"]
for doc in collection.find({"status": {"$in": ["active", "pending"]}}):
    print(doc)



'''
Logical Operators:
• $and 
• $or 
• $not 
• $nor
'''
# Age > 30 AND city = "New York"
for doc in collection.find({"$and": [{"age": {"$gt": 30}}, {"city": "New York"}]}):
    print(doc)

# Age > 30 OR status = "inactive"
for doc in collection.find({"$or": [{"age": {"$gt": 30}}, {"status": "inactive"}]}):
    print(doc)


'''
Regular Expressions: 
'''
# Name starts with "J" (case-insensitive)
import re
for doc in collection.find({"name": {"$regex": "^J", "$options": "i"}}):
    print(doc)



'''
Query on Arrays:
'''
# Tags include "python"
for doc in collection.find({"tags": "python"}):  # Exact element match
    print(doc)

# Tags include both "python" and "mongodb"
for doc in collection.find({"tags": {"$all": ["python", "mongodb"]}}):
    print(doc)

# Size of array = 3
for doc in collection.find({"tags": {"$size": 3}}):
    print(doc)



'''
Query on Nested/Embedded Documents:
'''
# Exact match on nested object
for doc in collection.find({"address": {"city": "New York", "zip": "10001"}}):
    print(doc)

# Match specific nested field
for doc in collection.find({"address.city": "New York"}):
    print(doc)


'''
Projection (Select Specific Fields)
Exclude unnecessary fields (e.g., _id).
'''
# Include only name and age, exclude _id
for doc in collection.find({"age": {"$gt": 30}}, {"name": 1, "age": 1, "_id": 0}):
    print(doc)



'''
Sorting, Limiting, Skipping:
'''
# Sort by age descending, limit to 10
cursor = collection.find().sort("age", -1).limit(10)

# Skip first 5, limit 10 (pagination)
cursor = collection.find().skip(5).limit(10)



'''
Counting Documents:
'''
count = collection.count_documents({"status": "active"})
print(count)



'''
Distinct Values:
'''
distinct_tags = collection.distinct("tags")
print(distinct_tags)



'''
Basic Aggregation Pipeline
For more complex operations (grouping, summing, etc.):
'''
pipeline = [
    {"$match": {"status": "active"}},                  # Filter
    {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}},  # Group & sum
    {"$sort": {"total": -1}}                           # Sort descending
]

for result in collection.aggregate(pipeline):
    print(result)