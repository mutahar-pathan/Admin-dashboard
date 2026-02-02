from app.models.orders_model import Orders
from app.database.db import order_collection

def create_order(orders : Orders):
    order_collection.insert_one(orders.dict())
    return{"message : order created"}


