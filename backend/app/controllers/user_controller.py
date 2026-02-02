from app.models.user_models import User
from app.database.db import users_collection , auth_user

def create_user(user : User):
    users_collection.insert_one(user.dict())
    return{"message : user created"}

def register(user : User):
    auth_user.insert_one(user.dict())
    return{"message : register successfully"}

def get_users():
    users = list(users_collection.find({}, {"_id": 0}))
    return {"users": users}
