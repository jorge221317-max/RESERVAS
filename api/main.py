from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import routes

app = FastAPI()

# Incluir rutas
app.include_router(routes.router)

# Archivos estáticos
app.mount("/static", StaticFiles(directory="api/static"), name="static")
