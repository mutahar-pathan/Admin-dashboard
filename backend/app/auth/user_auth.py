from app.models.user_auth import Register
from app.database.db import auth_user

def register_user(register : Register):
    auth_user.insert_one(register.dict())
    return{"message : register successfully"}



 