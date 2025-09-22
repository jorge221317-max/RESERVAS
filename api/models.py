from sqlalchemy import Column, Integer, String, DateTime, create_engine, MetaData, Table

DATABASE_URL = "sqlite:///./turnos.db"

metadata = MetaData()

turnos = Table(
    "turnos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String, nullable=False),
    Column("fecha_hora", DateTime, nullable=False)
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
