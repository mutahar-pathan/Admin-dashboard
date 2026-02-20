from fastapi import APIRouter
from api.products.product import product

product_router = APIRouter()

product_router.include_router(product, prefix="/product")