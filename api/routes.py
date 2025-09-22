from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from .database import database
from .models import turnos

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    query = turnos.select()
    resultados = await database.fetch_all(query)
    return templates.TemplateResponse("index.html", {"request": request, "turnos": resultados})

@router.post("/reservar", response_class=HTMLResponse)
async def reservar_turno(request: Request, nombre: str = Form(...), fecha_hora: str = Form(...)):
    fecha = datetime.fromisoformat(fecha_hora)
    query = turnos.insert().values(nombre=nombre, fecha_hora=fecha)
    await database.execute(query)
    query = turnos.select()
    resultados = await database.fetch_all(query)
    return templates.TemplateResponse("index.html", {"request": request, "turnos": resultados, "mensaje": "Turno confirmado!"})
