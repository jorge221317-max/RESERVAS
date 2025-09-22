from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import routes

app = FastAPI()

# Incluir las rutas desde routes.py
app.include_router(routes.router)

# Montar carpeta estática
app.mount("/static", StaticFiles(directory="api/static"), name="static")
