from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .routes import router, crear_turno, listar_turnos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Reservas")
app.include_router(router)

templates = Jinja2Templates(directory="api/templates")
app.mount("/static", StaticFiles(directory="api/static"), name="static")

@app.get("/")
def root(request: Request, db: Session = Depends(get_db)):
    turnos = listar_turnos(db)
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})

@app.post("/agregar_turno")
def agregar_turno(request: Request,
                  fecha_hora: str = Form(...),
                  usuario_id: int = Form(...),
                  db: Session = Depends(get_db)):
    crear_turno({"fecha_hora": fecha_hora, "usuario_id": usuario_id}, db)
    turnos = listar_turnos(db)
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})
