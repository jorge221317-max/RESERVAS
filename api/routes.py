from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter()

# Dependencia para obtener la sesión de BD
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/turnos", response_model=schemas.TurnoResponse)
def crear_turno(turno: schemas.TurnoCreate, db: Session = Depends(get_db)):
    db_turno = models.Turno(nombre=turno.nombre, fecha_hora=turno.fecha_hora)
    db.add(db_turno)
    db.commit()
    db.refresh(db_turno)
    return db_turno

@router.get("/turnos", response_model=list[schemas.TurnoResponse])
def listar_turnos(db: Session = Depends(get_db)):
    return db.query(models.Turno).all()
