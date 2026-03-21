from pydantic import BaseModel,ConfigDict

class ItemCreate(BaseModel):
    name: str
    price: float
    quantity: int

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

model_config = ConfigDict(from_attributes=True)