from app.models.user_auth import Register , Login
from app.database.db import auth_user
from fastapi import HTTPException , APIRouter

auth_router = APIRouter()

@auth_router.post("/register")
def register_user(register : Register):
    if auth_user.find_one({"email" : register.email}):
        raise HTTPException(
            status_code = 400,
            detail = "Email already registered"
        )
    auth_user.insert_one(register.dict())

    return{
        "message : register successfully"
    }
 
 def login_user(login : Login):
    auth_user.find
