from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- Configuración de DB (SQLite local) ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./turnos.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Modelo de Turnos ---
class Turno(Base):
    __tablename__ = "turnos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    fecha = Column(String, index=True)
    hora = Column(String, index=True)

Base.metadata.create_all(bind=engine)

# --- App FastAPI ---
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    db = SessionLocal()
    turnos = db.query(Turno).all()
    db.close()

    html = """
    <h2>📅 Sistema de Turnos</h2>
    <form method="post" action="/reservar">
        Nombre: <input type="text" name="nombre" required><br>
        Fecha: <input type="date" name="fecha" required><br>
        Hora: <input type="time" name="hora" required><br>
        <button type="submit">Reservar</button>
    </form>
    <br>
    <h3>Turnos Confirmados</h3>
    <table border="1" cellpadding="5">
        <tr><th>ID</th><th>Nombre</th><th>Fecha</th><th>Hora</th></tr>
    """
    for t in turnos:
        html += f"<tr><td>{t.id}</td><td>{t.nombre}</td><td>{t.fecha}</td><td>{t.hora}</td></tr>"
    html += "</table>"
    return html

@app.post("/reservar", response_class=HTMLResponse)
def reservar(nombre: str = Form(...), fecha: str = Form(...), hora: str = Form(...)):
    db = SessionLocal()
    nuevo = Turno(nombre=nombre, fecha=fecha, hora=hora)
    db.add(nuevo)
    db.commit()
    db.close()
    return f"""
    <h2>✅ Turno confirmado</h2>
    <p>{nombre} - {fecha} {hora}</p>
    <a href='/'>Volver</a>
    """
