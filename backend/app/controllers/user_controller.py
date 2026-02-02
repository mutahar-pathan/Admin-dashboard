from app.models.user_models import User
from app.database.db import users_collection

def create_user(user : User):
    users_collection.insert_one(user.dict())
    return{"message : user created"}



