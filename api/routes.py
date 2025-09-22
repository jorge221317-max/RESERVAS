from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from .models import Turno
from .database import SessionLocal

router = APIRouter()  # 👈 ESTE es el que faltaba

templates = Jinja2Templates(directory="api/templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    db = SessionLocal()
    turnos = db.query(Turno).all()
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})

@router.post("/turnos")
def crear_turno(turno: Turno):
    db = SessionLocal()
    db.add(turno)
    db.commit()
    db.refresh(turno)
    return turno

@router.get("/turnos")
def listar_turnos():
    db = SessionLocal()
    return db.query(Turno).all()
