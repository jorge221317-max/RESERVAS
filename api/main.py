from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Reservas")
app.include_router(router)

# Templates
templates = Jinja2Templates(directory="api/templates")

# Static
app.mount("/static", StaticFiles(directory="api/static"), name="static")

# Página principal
@app.get("/", response_model=None)
def root(request: Request):
    from .routes import listar_turnos
    return listar_turnos(request)
