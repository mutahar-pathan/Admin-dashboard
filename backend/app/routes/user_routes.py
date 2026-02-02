from app.controllers.user_controller import create_user
from app.models.user_models import User
from fastapi import APIRouter

user_router = APIRouter()

@user_router.post("/create_user")
def add_user(user : User):
    return create_user(user)



