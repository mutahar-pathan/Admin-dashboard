from api.auth.router import auth_router
from fastapi import APIRouter

route = APIRouter()

route.include_router(auth_router, tags=["AUTH"])