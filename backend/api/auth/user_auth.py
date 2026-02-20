from models.auth import Register,Login
from database.db import auth_user
from fastapi import HTTPException , APIRouter , Depends
from api.auth.password import hash_password , verify_password
from api.auth.token import create_access_token
from api.auth.roles import admin_only,user_only

router = APIRouter()

# @auth_router.post("/register")
# def register_user(register : Register):
#     if auth_user.find_one({"email" : register.email}):
#         raise HTTPException(
#             status_code = 400,
#             detail = "Email already registered"
#         )
#     auth_user.insert_one(register.dict())

#     return{``
#         "message" : "register successfully"
#     }


@router.post("/register")
def register_user(register: Register):
    if auth_user.find_one({"email": register.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    user_data = register.dict()
    user_data["password"] = hash_password(register.password)
    user_data["role"] = "user" 

    auth_user.insert_one(user_data)

    return {"message": "register successfully"}



# @auth_router.post("/login")
# def login_user(login: Login):
#     user = auth_user.find_one(
#         {
#             "email": login.email,
#             "password": login.password
#         },
#         {"_id": 0}
#     )

#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )

#     return {
#         "message": "Login successfully",
#         "role": user["role"],
#         "user": user
#     }

@router.post("/login")
def login_user(login: Login):
    user = auth_user.find_one({"email": login.email})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(login.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    token = create_access_token({
        "user_id": str(user["_id"]),
        "email": user["email"],
        "role": user.get("role", "user")
    }) 

    return {
        "message": "login successfully",
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }

@router.get("/dashboard")
def dashboard(user=Depends(admin_only)):
    return {
        "message": "Welcome Admin",
        "email": user["email"]
    }

@router.get("/me")
def me(user=Depends(user_only)):
    return user