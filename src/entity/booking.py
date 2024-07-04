from pydantic import BaseModel
from datetime import date

class Booking(BaseModel):
    car_id: int
    place_id: int
    created_at: date
    expired_at: date

    class Config:
        from_attributes = True