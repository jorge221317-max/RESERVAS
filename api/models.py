from pydantic import BaseModel

class Turno(BaseModel):
    id: int
    nombre: str
    fecha: str
    hora: str

    class Config:
        from_attributes = True
