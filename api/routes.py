from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import insert, select
from databases import Database
from .models import turnos

router = APIRouter()
templates = Jinja2Templates(directory="api/templates")
db = Database("sqlite:///turnos.db")

@router.on_event("startup")
async def startup():
    await db.connect()
    # Crear tabla si no existe
    query = "CREATE TABLE IF NOT EXISTS turnos (id INTEGER PRIMARY KEY, nombre TEXT, fecha TEXT, hora TEXT)"
    await db.execute(query)

@router.on_event("shutdown")
async def shutdown():
    await db.disconnect()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    query = turnos.select()
    lista_turnos = await db.fetch_all(query)
    return templates.TemplateResponse("index.html", {"request": request, "turnos": lista_turnos})

@router.post("/agregar")
async def agregar_turno(nombre: str = Form(...), fecha: str = Form(...), hora: str = Form(...)):
    query = insert(turnos).values(nombre=nombre, fecha=fecha, hora=hora)
    await db.execute(query)
    return {"message": "Turno agregado con éxito"}
