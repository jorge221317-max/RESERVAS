from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes import router
from .database import init_db, SessionLocal
from .models import Turno

app = FastAPI(title="Sistema de Turnos")

# Inicializar DB
init_db()

# Static y Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Rutas API
app.include_router(router)

# Página principal con tabla de turnos
@app.get("/")
def home(request: Request):
    db = SessionLocal()
    turnos = db.query(Turno).order_by(Turno.fecha).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})
