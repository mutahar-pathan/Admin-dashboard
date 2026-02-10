from fastapi import FastAPI , Depends
from app.auth.token import verify_token
from app.router.product_routes import product_router


app = FastAPI()

@app.get("/")
def read_root():
    return{"message : hello world"}

@app.get("/verify-token")
def verify(user = Depends(verify_token)):
    return {
        "message": "Token is valid",
        "user": user
    }

app.include(product_router)
