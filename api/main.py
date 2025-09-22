from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from .database import Base, engine, get_db
from .routes import router
from sqlalchemy.orm import Session
from .routes import listar_turnos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Reservas")
app.include_router(router)

templates = Jinja2Templates(directory="api/templates")

@app.get("/")
def root(request: Request, db: Session = Depends(get_db)):
    turnos = listar_turnos(db)
    return templates.TemplateResponse("turnos.html", {"request": request, "turnos": turnos})
