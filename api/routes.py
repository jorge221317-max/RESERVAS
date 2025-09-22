from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from .models import Turno, Usuario
from .utils import enviar_email

router = APIRouter()

def crear_turno(turno_data: dict, db: Session):
    from datetime import datetime
    fecha_hora = datetime.fromisoformat(turno_data["fecha_hora"])
    usuario_id = turno_data["usuario_id"]
    
    turno_existente = db.query(Turno).filter(Turno.fecha_hora == fecha_hora).first()
    if turno_existente:
        raise HTTPException(status_code=400, detail="Ya existe un turno en esa fecha y hora")
    
    nuevo_turno = Turno(fecha_hora=fecha_hora, usuario_id=usuario_id)
    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)

    usuario = db.query(Usuario).get(usuario_id)
    if usuario:
        enviar_email(usuario.email, "Turno confirmado", f"Tu turno es el {fecha_hora}")
    return nuevo_turno

def listar_turnos(db: Session):
    return db.query(Turno).all()

@router.delete("/turnos/{turno_id}")
def eliminar_turno(turno_id: int, db: Session):
    turno = db.query(Turno).get(turno_id)
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    db.delete(turno)
    db.commit()
    return {"detail": f"Turno {turno_id} eliminado"}
