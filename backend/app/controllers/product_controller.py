from app.models.product_model import Product
from app.database.db import product_collection

def create_product(product : Product):
    product_collection.insert_one(product.dict())
    return{"message : product created"}

