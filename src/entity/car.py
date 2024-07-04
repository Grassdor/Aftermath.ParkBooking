from pydantic import BaseModel

class Car(BaseModel):
    id: int
    number: str
    client: int

    class Config:
        from_attributes = True