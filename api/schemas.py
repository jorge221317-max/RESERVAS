from pydantic import BaseModel
from .models import Turno

class TurnoSchema(BaseModel):
    id: int
    nombre: str
    fecha: str
    hora: str

    class Config:
        from_attributes = True
