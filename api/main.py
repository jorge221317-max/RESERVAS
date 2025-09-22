from fastapi import FastAPI
from .database import Base, engine
from .routes import router

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Reservas")
app.include_router(router)

# Endpoint raíz para verificar que la app está online
@app.get("/")
def root():
    return {"message": "Bienvenido al Sistema de Reservas"}
