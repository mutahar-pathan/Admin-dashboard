from app.controllers.user_controller import create_user , register
from app.models.user_models import User
from fastapi import APIRouter

user_router = APIRouter()

@user_router.post("/create_user")
def add_user(user : User):
    return create_user(user)

@user_router.post("/register")
def register_user(user : User):
    return register(user)



