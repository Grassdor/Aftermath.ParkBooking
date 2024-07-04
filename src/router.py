from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.entity.booking import Booking
from src.repository.booking_repository import BookingRepository

router = APIRouter(
    prefix="/api"
)

@router.post("/create_book", status_code=201)
async def create_book(booking: Booking) -> JSONResponse:
    booking_id = await BookingRepository.add_one(booking)
    return {"id": booking_id}

@router.get("/get_booking", response_model=list[Booking])
async def get_booking() -> Booking:
    bookings = await BookingRepository.list_all()
    return bookings
