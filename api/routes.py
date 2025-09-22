from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .database import database
from .models import turnos

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    query = turnos.select()
    results = await database.fetch_all(query)
    return templates.TemplateResponse("index.html", {"request": request, "turnos": results})

@router.post("/turnos/", response_class=HTMLResponse)
async def agregar_turno(
    request: Request,
    nombre: str = Form(...),
    fecha: str = Form(...),
    hora: str = Form(...)
):
    query = turnos.insert().values(nombre=nombre.upper(), fecha=fecha, hora=hora)
    await database.execute(query)
    query_all = turnos.select()
    results = await database.fetch_all(query_all)
    return templates.TemplateResponse("index.html", {"request": request, "turnos": results})
