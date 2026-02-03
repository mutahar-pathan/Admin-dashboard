from pydantic import BaseModel
from typing import Literal

class Register(BaseModel):
    name : str
    email : str
    password : str
    role: Literal["user", "admin"] = "user"

class Login(BaseModel):
    email : str
    password : str

