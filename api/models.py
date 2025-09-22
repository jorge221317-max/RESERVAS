from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

DATABASE_URL = "sqlite:///./turnos.db"
database = Database(DATABASE_URL)
metadata = MetaData()

turnos = Table(
    "turnos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String, nullable=False),
    Column("fecha", String, nullable=False),
    Column("hora", String, nullable=False),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
