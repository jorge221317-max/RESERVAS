from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import database, metadata, engine
from . import routes

app = FastAPI(title="API de Reservas 🚀")

# Monta la carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="api/static"), name="static")

# Crea tablas si no existen
metadata.create_all(engine)

# Incluye rutas
app.include_router(routes.router)

# Conexión a la DB
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
