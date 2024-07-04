from pydantic import BaseModel

class Place(BaseModel):
    id: int
    price: float
    active: bool

    class Config:
        from_attributes = True