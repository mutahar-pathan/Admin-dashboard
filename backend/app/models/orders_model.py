from pydantic import BaseModel

class Orders(BaseModel):
    amount : str