from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import engine, turnos
from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime

app = FastAPI(title="Sistema de Turnos Funcional 🚀")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def leer_turnos(request: Request):
    with Session(engine) as session:
        query = select(turnos)
        resultados = session.execute(query).all()
    return templates.TemplateResponse("index.html", {"request": request, "turnos": resultados})

@app.post("/agregar_turno")
def agregar_turno(nombre: str = Form(...), fecha_hora: str = Form(...)):
    fecha_dt = datetime.fromisoformat(fecha_hora)
    with Session(engine) as session:
        session.execute(turnos.insert().values(nombre=nombre, fecha_hora=fecha_dt))
        session.commit()
    return {"mensaje": "Turno confirmado"}
