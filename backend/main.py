from fastapi import FastAPI
from app.routes.user_routes import user_router
from app.routes.product_routes import product_router
from app.routes.order_routes import order_router
from app.auth.user_auth import auth_router


app = FastAPI()

@app.get("/")
def read_root():
    return{"message : hello world"}

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(auth_router)
