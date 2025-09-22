from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from .models import Turno
from .schemas import TurnoSchema
from fastapi.templating import Jinja2Templates
from pathlib import Path

templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))

router = APIRouter()

# Base de datos temporal
turnos_db = [
    Turno(id=1, nombre="JUAN PEREZ", fecha="2025-09-22", hora="10:00"),
]

@router.get("/turnos", response_class=HTMLResponse)
async def listar_turnos(request: Request):
    turnos = [TurnoSchema.from_orm(t) for t in turnos_db]
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})

@router.post("/turnos/nuevo", response_class=HTMLResponse)
async def crear_turno(request: Request, nombre: str = Form(...), fecha: str = Form(...), hora: str = Form(...)):
    nuevo_id = len(turnos_db) + 1
    turno = Turno(id=nuevo_id, nombre=nombre.upper(), fecha=fecha, hora=hora)
    turnos_db.append(turno)
    turnos = [TurnoSchema.from_orm(t) for t in turnos_db]
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})
