from fastapi import FastAPI
from app.routes.user_routes import user_router

app = FastAPI()

@app.get("/")
def read_root():
    return{"message : hello world"}

app.include_router(user_router)
