from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Turno
from routes import listar_turnos, crear_turno

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Archivos estáticos (css, imágenes, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates Jinja2
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root(request: Request, db: Session = Depends(get_db)):
    return listar_turnos(request, db)


@app.post("/turnos")
def add_turno(request: Request, db: Session = Depends(get_db)):
    return crear_turno(request, db)
