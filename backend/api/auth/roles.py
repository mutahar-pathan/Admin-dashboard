from fastapi import Depends, HTTPException, status
from bson import ObjectId
from api.auth.token import verify_token
from database.db import auth_user
from utils.serializer import serialize_user


def get_current_user(payload=Depends(verify_token)):
    user_id = payload.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = auth_user.find_one(
        {"_id": ObjectId(user_id)}
    )

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return serialize_user(user) 


def admin_only(current_user=Depends(get_current_user)):
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access only"
        )
    return current_user


def user_only(current_user=Depends(get_current_user)):
    if current_user.get("role") not in ["user", "admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User access only"
        )
    return current_user
