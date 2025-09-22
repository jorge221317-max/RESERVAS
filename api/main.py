from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import router as routes_router

app = FastAPI(title="API de Reservas 🚀")

# Montar carpeta static
app.mount("/static", StaticFiles(directory="api/static"), name="static")

# Incluir rutas
app.include_router(routes_router)

@app.get("/")
async def root():
    return {"message": "API de Reservas funcionando 🚀"}
