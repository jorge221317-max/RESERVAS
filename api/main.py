from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Reservas")
app.include_router(router)

# Templates
templates = Jinja2Templates(directory="api/templates")

# Endpoint raíz para página interactiva
@app.get("/")
def root(request: Request):
    from .routes import listar_turnos
    db = next(router.dependant_dependencies[0].dependency())  # obtener session
    turnos = listar_turnos(db)
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})
