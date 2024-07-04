from pydantic import BaseModel
from datetime import datetime

class Client(BaseModel):
    id: int
    name: str
    phone: str
    created_at: datetime

    class Config:
        from_attributes = True