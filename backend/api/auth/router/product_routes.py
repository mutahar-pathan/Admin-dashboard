from app.models.product_model import Product
from fastapi import APIRouter
from database.db import product_collection

product_router = APIRouter()

@product_router.post("/add_product")
def add_product(product : Product):
    product_collection.insert_one(product.dict())
    return{"message" : "product added successfully"}




