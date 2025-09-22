from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

router = APIRouter()

templates = Jinja2Templates(directory="api/templates")

# Lista de turnos simulada (puede reemplazarse por DB)
turnos = []

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})

@router.post("/reservar", response_class=HTMLResponse)
async def reservar_turno(request: Request, nombre: str = Form(...), fecha: str = Form(...), hora: str = Form(...)):
    """
    Recibe datos del formulario y agrega un turno.
    """
    try:
        turno = {
            "nombre": nombre.upper(),
            "fecha": fecha,
            "hora": hora
        }
        turnos.append(turno)
        message = f"Turno reservado para {nombre.upper()} el {fecha} a las {hora} 🚀"
    except Exception as e:
        message = f"Error al reservar el turno: {str(e)}"

    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos, "message": message})
