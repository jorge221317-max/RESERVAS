from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Turno(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    fecha_hora = Column(DateTime, default=datetime.utcnow)
