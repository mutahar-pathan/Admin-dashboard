from fastapi import APIRouter
from app.controllers.product_controller import create_product
from app.models.product_model import Product

product_router = APIRouter()

@product_router.post("/create_product")
def add_product(product : Product):
    return create_product(product)