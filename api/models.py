from sqlalchemy import Table, Column, Integer, String, Date, Time
from .database import metadata

turnos = Table(
    "turnos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String, nullable=False),
    Column("fecha", String, nullable=False),
    Column("hora", String, nullable=False),
)
