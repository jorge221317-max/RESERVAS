from fastapi import FastAPI
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Reservas")
app.include_router(router)

# Endpoint raíz para evitar 404
@app.get("/")
def root():
    return {"message": "Bienvenido al Sistema de Reservas"}
