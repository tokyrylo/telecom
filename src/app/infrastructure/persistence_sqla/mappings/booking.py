from sqlalchemy import Column, DateTime, ForeignKey, Integer, Table
from sqlalchemy.orm import composite

from app.domain.value_objects.booking_id import BookingId
from app.domain.value_objects.room_id import RoomId
from app.domain.value_objects.user_id import UserId
from app.infrastructure.booking.model import Booking
from app.infrastructure.persistence_sqla.registry import mapping_registry

booking_table = Table(
    "booking",
    mapping_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("room_id", Integer, ForeignKey("rooms.id"), nullable=False),
    Column("user_id", Integer, nullable=False),
    Column("start_time", DateTime, nullable=False),
    Column("end_time", DateTime, nullable=False),
)


def map_booking_table() -> None:
    mapping_registry.map_imperatively(
        Booking,
        booking_table,
        properties={
            "id_": composite(BookingId, booking_table.c.id),
            "room_id_": composite(RoomId, booking_table.c.room_id),
            "user_id_": composite(UserId, booking_table.c.user_id),
            "start_time_": booking_table.c.start_time,
            "end_time_": booking_table.c.end_time,
        },
        column_prefix="_",
    )
