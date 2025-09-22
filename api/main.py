from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.routes import router as turnos_router
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Plantillas
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Incluir rutas de turnos
app.include_router(turnos_router)

# Ruta principal
@app.get("/", response_class="html")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
