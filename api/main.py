from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()

# Carpeta de templates
templates = Jinja2Templates(directory="templates")

# Carpeta de archivos estáticos (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Lista en memoria para guardar los turnos
turnos = []

# Página principal
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})

# Agregar un turno
@app.post("/agregar_turno", response_class=HTMLResponse)
async def agregar_turno(
    request: Request,
    nombre: str = Form(...),
    fecha: str = Form(...),
    hora: str = Form(...)
):
    try:
        turno = {
            "nombre": nombre.upper(),
            "fecha": fecha,
            "hora": hora,
            "confirmado": True
        }
        turnos.append(turno)
        mensaje = f"Turno para {nombre.upper()} confirmado!"
    except Exception as e:
        mensaje = f"Error al agregar turno: {str(e)}"
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos, "mensaje": mensaje})
