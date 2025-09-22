from pydantic import BaseModel
from datetime import datetime

class Turno(BaseModel):
    id: int
    fecha: str
    hora: str
    reservado: bool = False

    model_config = {
        "from_attributes": True  # reemplaza orm_mode
    }
