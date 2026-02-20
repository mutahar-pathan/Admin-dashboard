from fastapi import FastAPI , Depends
from api.auth.token import verify_token
from api.router.route import auth_router


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

app.include_router(auth_router)