from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, BOOLEAN, DATE, ForeignKey
from datetime import date, datetime
from src.settings import settings



engine = create_async_engine(
    settings.postgres_dsn
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(AsyncAttrs, DeclarativeBase):
    pass

class BookingOrm(Model):
    __tablename__ = "booking"

    id: Mapped[int] = mapped_column(primary_key=True)
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"), nullable=False)
    place_id: Mapped[int] = mapped_column(ForeignKey("place.id"), nullable=False)
    created_at: Mapped[date] = mapped_column(type_=DATE, nullable=False)
    expired_at: Mapped[date] = mapped_column(type_=DATE, nullable=False)

    car: Mapped["CarOrm"] = relationship(back_populates="bookings")
    place: Mapped["PlaceOrm"] = relationship(back_populates="bookings")

class CarOrm(Model):
    __tablename__ = "car"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(type_=VARCHAR, nullable=False)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), nullable=False)

    bookings: Mapped[list["BookingOrm"]] = relationship(back_populates="car")
    client: Mapped["ClientOrm"] = relationship(back_populates="cars")

class ClientOrm(Model):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(type_=VARCHAR, nullable=False)
    phone: Mapped[str] = mapped_column(type_=VARCHAR)
    created_at: Mapped[datetime] = mapped_column(type_=TIMESTAMP, nullable=False)

    cars: Mapped[list["CarOrm"]] = relationship(back_populates="client")
    

class PlaceOrm(Model):
    __tablename__ = "place"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(type_=FLOAT, nullable=False)
    active: Mapped[bool] = mapped_column(type_=BOOLEAN, nullable=False)

    bookings: Mapped[list["BookingOrm"]] = relationship(back_populates="place")
