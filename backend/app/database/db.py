from pymongo import Mongoclient

MONGO_URl = "mongodb://localhost:27017"

client = Mongoclient(MONGO_URl)

db = client["Admin_Dashboard"]

print("mongodb connected successfully")
