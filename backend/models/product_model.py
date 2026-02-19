from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name : str
    price : Optional[str]
    quantity : Optional[str]
    image : Optional[str]
    amount : int
    
