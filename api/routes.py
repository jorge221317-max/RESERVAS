from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from api.models import SessionLocal, Turno
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/agregar-turno")
async def agregar_turno(request: Request, nombre: str = Form(...), email: str = Form(...), fecha_hora: str = Form(...)):
    db: Session = next(get_db())
    nuevo_turno = Turno(nombre=nombre, email=email, fecha_hora=fecha_hora)
    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)
    return RedirectResponse("/", status_code=303)

@router.get("/turnos")
async def ver_turnos(request: Request):
    db: Session = next(get_db())
    turnos = db.query(Turno).all()
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})
