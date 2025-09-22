from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from api.models import Base, Turno  # ✅ Importación correcta

# Configuración de la app
app = FastAPI()

# Configuración de templates
templates = Jinja2Templates(directory="templates")

# Base de datos SQLite
DATABASE_URL = "sqlite:///./reservas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas
Base.metadata.create_all(bind=engine)


@app.get("/", response_class=HTMLResponse)
async def leer_turnos(request: Request):
    """Página principal con la lista de turnos"""
    db = SessionLocal()
    turnos = db.query(Turno).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})


@app.post("/reservar")
async def reservar_turno(
    nombre: str = Form(...),
    fecha: str = Form(...),
    hora: str = Form(...)
):
    """Reservar un turno nuevo"""
    db = SessionLocal()
    fecha_hora = datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
    nuevo_turno = Turno(nombre=nombre, fecha_hora=fecha_hora)

    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)
    db.close()

    return RedirectResponse(url="/", status_code=303)
