'''
Sorting Query Results in PyMongo (Python MongoDB Driver)
In PyMongo, you sort results using the .sort() method on a cursor returned by find() or find_one() (though find_one() typically doesn't need sorting unless combined with other operations).

# Basic Syntax
cursor = collection.find(query).sort(field_name, direction)

• direction:
    • 1 or pymongo.ASCENDING → Ascending order (low to high)
    • -1 or pymongo.DESCENDING → Descending order (high to low)
'''
# Import Required Constants

from pymongo import ASCENDING, DESCENDING
# or
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]


# 1. Sort by one field (ascending)
for doc in collection.find().sort("age", ASCENDING):
    print(doc)


# 2. Sort by one field (descending)
for doc in collection.find().sort("age", DESCENDING):
    print(doc)


# 3. Sort by multiple fields (compound sort)
# First by 'city' ascending, then by 'age' descending
for doc in collection.find().sort([
    ("city", ASCENDING),
    ("age", DESCENDING)
]):
    print(doc)


# 4. With filter, projection, limit, and sort
results = collection.find(
    {"status": "active"},                  # Filter
    {"name": 1, "age": 1, "_id": 0}        # Projection
).sort("age", DESCENDING).limit(10)        # Sort + limit

for doc in results:
    print(doc)


# 5. Sort by nested field
# Sort by address.zip ascending
for doc in collection.find().sort("address.zip", ASCENDING):
    print(doc)


# 6. Sort by array field (first element)
# MongoDB sorts arrays by their elements in order. To sort by the first element:
for doc in collection.find().sort("tags.0", ASCENDING):
    print(doc)


# 7. Case-insensitive text sort (requires index)
# For true case-insensitive sorting, create a collation:
results = collection.find({"name": {"$exists": True}}).collation(
    {"locale": "en", "strength": 2}
).sort("name", ASCENDING)

for doc in results:
    print(doc)



'''
Performance Tips
    • Sorting is efficient when there's an index on the sorted field(s).
    • Create index:
'''
collection.create_index([("age", DESCENDING)])
# Or compound
collection.create_index([("city", ASCENDING), ("age", DESCENDING)])


'''
Common Pitfalls
    • find_one() with sort returns the first document in sorted order:
'''
youngest = collection.find().sort("age", ASCENDING).limit(1)[0]