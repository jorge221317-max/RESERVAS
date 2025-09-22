from fastapi import APIRouter, Form
from typing import List
from .models import Turno

router = APIRouter()

# Lista inicial de turnos
turnos_db = [
    Turno(id=1, fecha="2025-09-22", hora="10:00"),
    Turno(id=2, fecha="2025-09-22", hora="11:00"),
    Turno(id=3, fecha="2025-09-22", hora="12:00"),
]

@router.get("/turnos", response_model=List[Turno])
async def listar_turnos():
    return turnos_db

@router.post("/turnos/reservar")
async def reservar_turno(turno_id: int = Form(...)):
    for turno in turnos_db:
        if turno.id == turno_id:
            if turno.reservado:
                return {"message": "Turno ya reservado ❌"}
            turno.reservado = True
            return {"message": "Turno reservado con éxito 🚀"}
    return {"message": "Turno no encontrado"}
