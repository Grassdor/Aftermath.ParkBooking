from src.database import new_session, BookingOrm
from src.entity.booking import Booking
from sqlalchemy import select

class BookingRepository:
    @classmethod
    async def add_one(cls, data: Booking) -> int:
        async with new_session() as session:
            booking_dict = data.model_dump()

            booking = BookingOrm(**booking_dict)
            session.add(booking)
            await session.flush()
            await session.commit()
            return booking.id
    
    @classmethod
    async def list_all(csl):
        async with new_session() as session:
            query = select(BookingOrm)
            result = await session.execute(query)
            booking_entity = result.scalars().all()
            return booking_entity