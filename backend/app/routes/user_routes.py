from app.controllers.user_controller import create_user , register, get_users
from app.models.user_models import User
from fastapi import APIRouter

user_router = APIRouter()

@user_router.post("/create_user")
def add_user(user : User):
    return create_user(user)

@user_router.post("/register")
def register_user(user : User):
    return register(user)

@user_router.get("/users")
def fetch_users():
    return get_users()


