from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Turno
from datetime import datetime

router = APIRouter()

# Crear turno con fecha y hora
@router.post("/turnos/")
def crear_turno(nombre: str, fecha_hora: str, db: Session = Depends(get_db)):
    try:
        dt = datetime.fromisoformat(fecha_hora)
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha/hora inválido")
    turno = Turno(nombre=nombre, fecha_hora=dt)
    db.add(turno)
    db.commit()
    db.refresh(turno)
    return {"message": "Turno creado", "turno": {"id": turno.id, "nombre": turno.nombre, "fecha_hora": turno.fecha_hora}}

# Listar turnos
@router.get("/turnos/")
def listar_turnos(db: Session = Depends(get_db)):
    return db.query(Turno).order_by(Turno.fecha_hora).all()

# Eliminar turno
@router.delete("/turnos/{turno_id}")
def eliminar_turno(turno_id: int, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == turno_id).first()
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    db.delete(turno)
    db.commit()
    return {"message": "Turno eliminado"}
