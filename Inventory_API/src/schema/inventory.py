from pydantic import BaseModel

class Inventory(BaseModel):
    item: str
    price_per_unit: float
    quantity: float
    unit: float

    class Config:
        orm_mode=True
