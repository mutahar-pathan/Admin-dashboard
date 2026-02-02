from pymongo import MongoClient

MONGO_URl = "mongodb://localhost:27017"

client = MongoClient(MONGO_URl)

db = client["Admin_Dashboard"]

users_collection = db["users"]

print("mongodb connected successfully")
