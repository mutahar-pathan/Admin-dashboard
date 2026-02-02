from pymongo import MongoClient

MONGO_URl = "mongodb://localhost:27017"

client = MongoClient(MONGO_URl)

db = client["Admin_Dashboard"]

users_collection = db["users"]
product_collection  = db["product"]
order_collection = db["orders"]
auth_user = db["auth"]

print("mongodb connected successfully")
