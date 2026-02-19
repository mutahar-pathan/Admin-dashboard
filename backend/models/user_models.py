from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name : str
    age : str
    email : str
    password : Optional[str]
