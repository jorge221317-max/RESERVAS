from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes import router, listar_turnos
from .database import Base, engine

# Crear tablas
Base.metadata.create_all(bind=engine)

# App
app = FastAPI(title="Sistema de Reservas")
app.include_router(router)

# Montar carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="api/static"), name="static")

# Templates
templates = Jinja2Templates(directory="api/templates")

# Página principal
@app.get("/")
def root(request: Request):
    db = next(router.dependant_dependencies[0].dependency())  # obtener session
    turnos = listar_turnos(db)
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})
