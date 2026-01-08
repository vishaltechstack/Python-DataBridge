'''
The .limit() method restricts the number of documents returned by a find() query (or any cursor).
It's commonly used for pagination, performance optimization, or when you only need a few results.
'''
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# 1. Limit to 5 documents
for doc in collection.find().limit(5):
    print(doc)


# 2. With filter and projection
results = collection.find(
    {"status": "active"},              # Filter
    {"name": 1, "age": 1, "_id": 0}     # Projection
).limit(10)                            # Limit to 10

for doc in results:
    print(doc)


# 3. Get just one document (alternative to find_one)
doc = collection.find({"name": "John"}).limit(1)[0]  # Returns first match
# Or convert to list (careful with large limits)
doc = list(collection.find({"name": "John"}).limit(1))[0]


# 4. Limit(0) behavior
collection.find().limit(0)


'''
5. Remove limit from a cursor
If you previously set a limit and want all results:
'''
cursor = collection.find().limit(10)
unlimited_cursor = cursor.limit(0)