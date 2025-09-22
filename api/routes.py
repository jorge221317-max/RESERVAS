from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session
from datetime import datetime
from .database import get_db
from .models import Turno

router = APIRouter()

# Crear turno
@router.post("/agregar_turno/", response_model=None)
def agregar_turno(
    request: Request,
    nombre: str = Form(...),
    fecha_hora: str = Form(...),
    db: Session = Depends(get_db)
):
    dt = datetime.fromisoformat(fecha_hora)
    nuevo_turno = Turno(nombre=nombre.upper(), fecha_hora=dt)
    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)
    turnos = db.query(Turno).order_by(Turno.fecha_hora).all()
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates(directory="api/templates")
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})

# Listar turnos
@router.get("/turnos/", response_model=None)
def listar_turnos(request: Request, db: Session = Depends(get_db)):
    turnos = db.query(Turno).order_by(Turno.fecha_hora).all()
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates(directory="api/templates")
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})

# Eliminar turno
@router.post("/eliminar_turno/", response_model=None)
def eliminar_turno(turno_id: int = Form(...), request: Request = None, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == turno_id).first()
    if turno:
        db.delete(turno)
        db.commit()
    turnos = db.query(Turno).order_by(Turno.fecha_hora).all()
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates(directory="api/templates")
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})
