from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="Sistema de Turnos")

# Modelo en memoria (sin base de datos todavía)
class Turno(BaseModel):
    id: int
    nombre: str
    fecha: str
    hora: str

# Lista de turnos en memoria
turnos: List[Turno] = []

@app.get("/")
def root():
    return {"message": "Sistema de Turnos activo 🚀"}

@app.get("/turnos")
def listar_turnos():
    return turnos

@app.post("/turnos")
def crear_turno(turno: Turno):
    # Validar duplicados por fecha y hora
    for t in turnos:
        if t.fecha == turno.fecha and t.hora == turno.hora:
            return {"error": "Ese turno ya está reservado ❌"}
    turnos.append(turno)
    return {"ok": "Turno reservado ✅", "turno": turno}
