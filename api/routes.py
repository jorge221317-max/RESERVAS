from fastapi import APIRouter
from .schemas import TurnoBase

router = APIRouter()

@router.get("/turnos")
def listar_turnos():
    return {"turnos": []}

@router.post("/turnos")
def crear_turno(turno: TurnoBase):
    return {"message": "Turno creado", "turno": turno}
