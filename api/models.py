from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import metadata

turnos = Table(
    "turnos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String, nullable=False),
    Column("fecha_hora", DateTime, nullable=False),
)
