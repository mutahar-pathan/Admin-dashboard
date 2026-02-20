from api.auth.router import auth_router
from fastapi import APIRouter
from api.products.router import product_router

route = APIRouter()

route.include_router(auth_router, tags=["AUTH"])
route.include_router(product_router,tags=["PRODUCT"])