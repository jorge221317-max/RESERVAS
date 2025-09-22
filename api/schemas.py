from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    rol: str = "usuario"

class UsuarioResponse(UsuarioBase):
    id: int
    rol: str
    class Config:
        orm_mode = True

class TurnoBase(BaseModel):
    fecha_hora: datetime

class TurnoCreate(TurnoBase):
    usuario_id: int

class TurnoResponse(TurnoBase):
    id: int
    usuario_id: int
    class Config:
        orm_mode = True
