from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session
from .database import get_db
from .models import Turno
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="api/templates")

@router.get("/")
def listar_turnos(request: Request, db: Session = Depends(get_db)):
    turnos = db.query(Turno).order_by(Turno.fecha_hora).all()
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})

@router.post("/turnos")
def crear_turno(
    request: Request,
    nombre: str = Form(...),
    fecha_hora: str = Form(...),
    db: Session = Depends(get_db)
):
    # Evitar duplicados
    exists = db.query(Turno).filter(Turno.nombre==nombre, Turno.fecha_hora==fecha_hora).first()
    if exists:
        turnos = db.query(Turno).all()
        return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos, "error": "Turno ya existente"})
    
    turno = Turno(nombre=nombre, fecha_hora=fecha_hora)
    db.add(turno)
    db.commit()
    db.refresh(turno)
    return RedirectResponse("/", status_code=303)

@router.get("/turnos/delete/{turno_id}")
def eliminar_turno(turno_id: int, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id==turno_id).first()
    if turno:
        db.delete(turno)
        db.commit()
    return RedirectResponse("/", status_code=303)
