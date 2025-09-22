from pydantic import BaseModel
from datetime import datetime

class TurnoBase(BaseModel):
    usuario_id: int
    fecha: datetime
    hora: str

    class Config:
        from_attributes = True  # reemplaza orm_mode = True
