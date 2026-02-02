from fastapi import APIRouter
from app.controllers.order_controller import create_order
from app.models.orders_model import Orders

order_router = APIRouter()

@order_router.post("/create_order")
def add_order(order : Orders):
    return create_order(order)

