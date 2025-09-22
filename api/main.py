from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes import router as turnos_router

app = FastAPI(title="Sistema de Turnos")

# Carpeta static y templates
app.mount("/static", StaticFiles(directory="api/static"), name="static")
templates = Jinja2Templates(directory="api/templates")

# Rutas
app.include_router(turnos_router)

@app.get("/")
async def root():
    return {"message": "Sistema de Turnos activo 🚀"}
