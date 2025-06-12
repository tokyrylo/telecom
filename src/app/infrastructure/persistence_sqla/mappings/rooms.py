from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import composite

from app.domain.value_objects.room_id import RoomId
from app.infrastructure.persistence_sqla.registry import mapping_registry
from app.infrastructure.rooms.model import Room

rooms_table = Table(
    "rooms",
    mapping_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("capacity", Integer),
)


def map_rooms_table() -> None:
    mapping_registry.map_imperatively(
        Room,
        rooms_table,
        properties={
            "id_": composite(RoomId, rooms_table.c.id),
            "name": rooms_table.c.name,
            "capacity": rooms_table.c.capacity,
        },
        column_prefix="_",
    )
