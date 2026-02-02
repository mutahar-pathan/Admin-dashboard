from pydantic import BaseModel
from typing import Literal


class User(BaseModel):
    name : str
    email : str
    password : str
    role : Literal["admin" , "user"]
