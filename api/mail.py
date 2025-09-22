from fastapi import FastAPI
from .routes import router

app = FastAPI(title="API de Reservas 🚀")
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "API de Reservas funcionando 🚀"}
