from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")     # Connect to MongoDB server
db = client["mydatabase"]  # Database created here (lazily on first insert)