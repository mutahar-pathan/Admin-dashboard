from app.controllers.user_controller import create_user , get_users
from app.models.user_models import User
from app.auth.roles import user_only
from fastapi import APIRouter , Depends

user_router = APIRouter()

@user_router.post("/create_user")
def add_user(user : User):
    return create_user(user)

@user_router.get("/users")
def fetch_users():
    return get_users()

@user_router.get("/me")
def me(user=Depends(user_only)):
    return user


