from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from .models import Turno, SessionLocal
import datetime

router = APIRouter()

@router.get("/turnos")
async def listar_turnos(request: Request):
    db = SessionLocal()
    turnos = db.query(Turno).all()
    db.close()
    return {"turnos": [{"id": t.id, "nombre": t.nombre, "fecha_hora": t.fecha_hora} for t in turnos]}

@router.post("/turnos")
async def agregar_turno(nombre: str = Form(...), fecha_hora: str = Form(...)):
    db = SessionLocal()
    dt = datetime.datetime.fromisoformat(fecha_hora)
    nuevo_turno = Turno(nombre=nombre, fecha_hora=dt)
    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)
    db.close()
    return RedirectResponse(url="/", status_code=303)
