from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Usuario, Turno
from .schemas import UsuarioCreate, UsuarioResponse, TurnoCreate, TurnoResponse
from .database import get_db
from .utils import enviar_email

router = APIRouter()

# Crear usuario
@router.post("/usuarios/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# Crear turno con validación de duplicados
@router.post("/turnos/", response_model=TurnoResponse)
def crear_turno(turno: TurnoCreate, db: Session = Depends(get_db)):
    turno_existente = db.query(Turno).filter(Turno.fecha_hora == turno.fecha_hora).first()
    if turno_existente:
        raise HTTPException(status_code=400, detail="Ya existe un turno en esa fecha y hora")
    
    nuevo_turno = Turno(**turno.dict())
    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)

    # Enviar email de confirmación
    usuario = db.query(Usuario).get(turno.usuario_id)
    enviar_email(usuario.email, "Turno confirmado", f"Tu turno es el {turno.fecha_hora}")
    
    return nuevo_turno
