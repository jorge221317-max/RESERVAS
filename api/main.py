from fastapi import FastAPI
from .database import database, metadata, engine
from .routes import router

# Crear tablas si no existen
metadata.create_all(engine)

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
