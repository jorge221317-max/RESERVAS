from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import routes  # importa tus rutas

app = FastAPI()

# Montar carpeta static (ajusta si tu static está dentro de api/)
app.mount("/static", StaticFiles(directory="api/static"), name="static")

# Endpoint raíz para test rápido
@app.get("/")
def root():
    return {"message": "API de Reservas funcionando 🚀"}

# Incluir rutas si tus rutas están definidas correctamente
# routes.py debe tener `router = APIRouter()` y tus endpoints
app.include_router(routes.router)
