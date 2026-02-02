from fastapi import FastAPI
from app.routes.user_routes import user_router
from app.routes.product_routes import product_router

app = FastAPI()

@app.get("/")
def read_root():
    return{"message : hello world"}

app.include_router(user_router)
app.include_router(product_router)
