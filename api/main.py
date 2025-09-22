from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
from datetime import datetime

app = FastAPI()

# Monta los archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Carpeta de templates
templates = Jinja2Templates(directory="templates")

# Conexión SQLite
def get_db():
    conn = sqlite3.connect("turnos.db")
    conn.row_factory = sqlite3.Row
    return conn

# Ruta principal para ver y agregar turnos
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS turnos (id INTEGER PRIMARY KEY, nombre TEXT, fecha TEXT, hora TEXT)")
    cursor.execute("SELECT * FROM turnos")
    turnos = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})

@app.post("/turno", response_class=HTMLResponse)
def crear_turno(request: Request, nombre: str = Form(...), fecha: str = Form(...), hora: str = Form(...)):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO turnos (nombre, fecha, hora) VALUES (?, ?, ?)", (nombre, fecha, hora))
    conn.commit()
    cursor.execute("SELECT * FROM turnos")
    turnos = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "turnos": turnos})
