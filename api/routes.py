from fastapi import Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from .models import Turno
from .database import get_db
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


# Mostrar lista de turnos
def listar_turnos(request: Request, db: Session):
    turnos = db.query(Turno).all()
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})


# Crear un nuevo turno
def crear_turno(
    request: Request,
    db: Session,
    nombre: str = Form(...),
    fecha_hora: str = Form(...)
):
    nuevo_turno = Turno(nombre=nombre, fecha_hora=fecha_hora)
    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)

    return RedirectResponse(url="/", status_code=303)
