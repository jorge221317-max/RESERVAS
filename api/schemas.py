from pydantic import BaseModel
from datetime import datetime

class TurnoBase(BaseModel):
    nombre: str
    fecha_hora: datetime

class TurnoCreate(TurnoBase):
    pass

class TurnoResponse(TurnoBase):
    id: int

    class Config:
        orm_mode = True  # 👈 Esto permite convertir desde modelos SQLAlchemy
