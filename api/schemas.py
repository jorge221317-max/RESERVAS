from pydantic import BaseModel
from datetime import datetime

class UsuarioCreate(BaseModel):
    nombre: str
    email: str

class UsuarioResponse(UsuarioCreate):
    id: int
    rol: str

    class Config:
        from_attributes = True

class TurnoCreate(BaseModel):
    fecha_hora: datetime
    usuario_id: int

class TurnoResponse(TurnoCreate):
    id: int

    class Config:
        from_attributes = True
