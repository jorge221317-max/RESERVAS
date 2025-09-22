from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Turno, Base
from datetime import datetime

Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_class=HTMLResponse)
def read_turnos(request: Request, db: Session = Depends(get_db)):
    turnos = db.query(Turno).order_by(Turno.fecha_hora).all()
    return request.app.templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})

@router.post("/reservar", response_class=HTMLResponse)
def reservar_turno(request: Request, nombre: str = Form(...), fecha_hora: str = Form(...), db: Session = Depends(get_db)):
    fecha_obj = datetime.strptime(fecha_hora, "%Y-%m-%dT%H:%M")
    nuevo_turno = Turno(nombre=nombre, fecha_hora=fecha_obj)
    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)
    return RedirectResponse("/", status_code=303)
