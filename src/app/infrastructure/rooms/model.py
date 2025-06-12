from dataclasses import dataclass

from app.domain.value_objects.room_id import RoomId


@dataclass(eq=True, kw_only=True)
class Room:
    room_id: RoomId
    name: str
    capacity: int
