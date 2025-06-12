from dataclasses import dataclass

from app.domain.value_objects.booking_id import BookingId
from app.domain.value_objects.room_id import RoomId
from app.domain.value_objects.user_id import UserId


@dataclass(eq=True, kw_only=True)
class Booking:
    id_: BookingId
    room_id_: RoomId
    user_id_: UserId
    start_time_: str
    end_time_: str
