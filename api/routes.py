from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
from .models import Turno
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/turnos/agregar")
def agregar_turno(nombre: str = Form(...), fecha: str = Form(...), db: Session = Depends(get_db)):
    from datetime import datetime
    fecha_dt = datetime.fromisoformat(fecha)
    nuevo_turno = Turno(nombre=nombre, fecha=fecha_dt)
    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)
    return {"message": "Turno agregado", "turno": {"id": nuevo_turno.id, "nombre": nuevo_turno.nombre, "fecha": nuevo_turno.fecha}}

@router.get("/turnos")
def listar_turnos(db: Session = Depends(get_db)):
    turnos = db.query(Turno).order_by(Turno.fecha).all()
    return {"turnos": [{"id": t.id, "nombre": t.nombre, "fecha": t.fecha} for t in turnos]}
