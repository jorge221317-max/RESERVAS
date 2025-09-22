from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .models import Turno, database

router = APIRouter()
templates = Jinja2Templates(directory="api/templates")

@router.get("/turnos", response_class=HTMLResponse)
async def ver_turnos(request: Request):
    query = "SELECT * FROM turnos"
    turnos = await database.fetch_all(query)
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})

@router.post("/turnos")
async def crear_turno(nombre: str = Form(...), fecha: str = Form(...), hora: str = Form(...)):
    query = "INSERT INTO turnos(nombre, fecha, hora) VALUES (:nombre, :fecha, :hora)"
    await database.execute(query, values={"nombre": nombre, "fecha": fecha, "hora": hora})
    return {"message": "Turno creado con éxito"}
