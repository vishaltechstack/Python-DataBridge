'''
Dropping a collection permanently deletes the collection and all its documents, indexes, and associated data.
This operation is irreversible, so use it with extreme caution.

When to use drop() vs delete_many({})

Action                  Use Case                                                          Keeps Indexes?           Keeps Collection?

delete_many({})         Remove all documents, keep collection & indexes                   Yes                      Yes
collection.drop()       Completely remove collection (faster for large data)              No                       No

'''
# Basic Method: drop()
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["your_database"]
collection = db["your_collection"]
collection.drop()   # Drop the entire collection

print("Collection dropped successfully")


'''
Alternative: Using the Database Object
You can also drop a collection by name directly from the database:
'''
# Drop collection by name
db.drop_collection("your_collection")

# Or using a Collection object
db.drop_collection(collection)


'''
Check If Collection Exists Before Dropping (Safer Approach)
Avoid errors if the collection doesn't exist:
'''
if "your_collection" in db.list_collection_names():
    collection.drop()
    print("Collection dropped")
else:
    print("Collection does not exist")


# Drop Multiple Collections
collections_to_drop = ["users", "logs", "temp_data"]

for coll_name in collections_to_drop:
    if coll_name in db.list_collection_names():
        db[coll_name].drop()
        print(f"{coll_name} dropped")


'''
Drop All Collections in a Database
Warning: This removes everything in the database!
'''
for coll_name in db.list_collection_names():
    db[coll_name].drop()
    print(f"Dropped: {coll_name}")