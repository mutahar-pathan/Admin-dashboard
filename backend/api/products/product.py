from models.product_model import Product
from fastapi import APIRouter
from database.db import product_collection
from bson import ObjectId

product = APIRouter()

@product.post("/add-products")
def add_product(product : Product):
    product_collection.insert_one(product.dict())
    return {"message" : "added product successfully"}
    
@product.get("/get-products")
def get_products():
    products = []
    for item in product_collection.find():
        item["_id"] = str(item["_id"])
        products.append(item)  
        return products
    
@product.put("/update-products")
def update_products(id:str , product : Product):
    product_collection.update_one(
        {"_id" : ObjectId(id)},
        {"$set" : product.dict()}
    )
    return {"message" : "product update successfully"}

@product.delete("/delete-products")
def delete_products(id:str):
    product_collection.delete_one({"_id" : ObjectId(id)})
    return {"message" : "product deleted successfully"}



